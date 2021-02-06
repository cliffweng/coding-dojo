import pandas as pd
import io, sys, requests

#from talib import *
#import alpaca_trade_api as alpaca
#import quandl
alpacaapi = None

## Replace below passcode with the real ones (passcode.txt)
AV_KEY = 'demo'
APCA-API-KEY-ID = 'xxxxxx'
APCA-API-SECRET-KEY = 'xxxxxx'

def alpacaInit():
    alpacaapi = alpaca.REST(APCA-API-KEY-ID, APCA-API-SECRET-KEY, 'https://paper-api.alpaca.markets')
    print ("AlpacaApi initialized")

def query2Filename(query):
    if sys.platform.startswith('win'):
        return ".cache/pickle/" + query.replace("/","") + ".pickle"
    else:
        return "~/.cache/pickle/" + query.replace("/","") + ".pickle"

def getCache(filename, query, verb):
    try: # try to load from cache first
        df = pd.read_pickle(filename)
        if verb:
            print ("["+query+"] retrieved from cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
        return df
    except Exception as e:
        return None

## Alpha Vantage Price
## mode : 'd' daily, 'm' : minute
def AVGet(ticker, mode='d', force=False, verb=True) :
    filename = query2Filename(ticker+'-'+mode)
    if not force:
        df = getCache(filename,ticker,verb)
        if isinstance(df, pd.DataFrame):
            return df
    print ("Querying Alpha Vantage " + ticker + " " + mode +  filename)
    func='TIME_SERIES_DAILY_ADJUSTED'
    if mode != 'd':
        func='TIME_SERIES_INTRADAY&interval='+mode
    df = pd.read_csv('https://www.alphavantage.co/query?function='+func+'&symbol='+
        ticker+'&apikey='+AVkey+'&outputsize=full&datatype=csv',index_col=0)
    # df.index.name = 'Date'
    df.to_pickle(filename)
    if verb:
        print (ticker + " saved to cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
    return df

## This function returns cache result from Quandl, if available. Otherwise, it downloads from Quandl
def QuandlGet(query, force=False, verb=True) :
    filename = query2Filename(query)
    if not force:
        df = getCache(filename,query,verb)
        if isinstance(df, pd.DataFrame):
            return df
    print ("Querying Quandl " + query + " "+filename)
    df = quandl.get(query)
    df.to_pickle(filename)
    if verb:
        print (query + " saved to cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
    return df

def AlpacaGet(query, force=False, verb=True) :
    filename = query2Filename(query)
    if not force:
        df = getCache(filename,query,verb)
        if isinstance(df, pd.DataFrame):
            return df
    print ("Querying Alpaca " + query + " "+filename)
    d= alpacaapi.get_barset(query, 'day').df
    df = d[query].rename(columns={'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'})
    df.index.name = 'Date'
    df.to_pickle(filename)
    if verb:
        print (query + " saved to cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
    return df

## This function returns cache result from Quandl, if available. Otherwise, it downloads from Quandl
def CSVGet(url, name, force=False, verb=True) :
    #filename = "../.cache/pickle/" + name + ".pickle"
    if sys.platform.startswith('win'):
        filename = ".cache/pickle/" + name + ".pickle"
    else:
        filename = "~/.cache/pickle/" + name + ".pickle"
    if not force:
        try: # try to load from cache first
            df = pd.read_pickle(filename)
            if verb:
                print ("["+name+"] retrieved from cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
            return df
        except Exception as e:
            print (e)
            pass
    print ("Retrieving CSV " + url + " "+name)
    s=requests.get(url).content
    df=pd.read_csv(io.StringIO(s.decode('utf-8')))
    df.to_pickle(filename)
    if verb:
        print (name + " saved to cache. Size="+str(df.index.size)+", Columns="+str(df.columns.values))
    return df

def getAllTechinicals(ticker):
    df = QuandlGet("WIKI/"+ticker, verb=False)
    return add_all_ta_features(df, "Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume", fillna=True)

def getAllTrendsTA(ticker):
    df = QuandlGet("WIKI/"+ticker, verb=False)
    return add_trend_ta(df, "Adj. High", "Adj. Low", "Adj. Close", fillna=True)

def getAllMomentumTA(ticker):
    df = QuandlGet("WIKI/"+ticker, verb=False)
    return add_momentum_ta(df, "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume", fillna=True)


## rename columns in a DF by appending 'name' to the column names
def rename(df,name) :
    lst = {}
    for col in df:
        if name :
            lst[col] = col +" ("+name+")"
    return df.rename(columns=lst)

## dfs : list of list[df, name] if need to rename
##     or df, if no need to rename
## clean : None, fill, drop
def merge(dfs, clean=None, append=False) :
    l = []
    for n in dfs:
        if type(n) is list:
            l.append(rename(n[0],n[1]))
        else:
            l.append(n)
    if append :
        res = pd.concat(l)
    else :
        res = pd.concat(l, axis=1)
    if clean == 'fill':
        return res.ffill().bfill()
    elif clean == 'drop':
        return res.dropna()
    elif clean == 'fill_drop':
        return res.ffill().bfill().dropna()
    elif clean == None:
        return res
    else:
        raise Exception('['+clean+'] is not supported')
