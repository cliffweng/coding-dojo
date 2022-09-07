This is Coding Dojo [(on Colab)](https://colab.research.google.com/github/cliffweng/coding-dojo/blob/master/Coding_Dojo_Overview.ipynb) developed by [Cliff Weng](https://github.com/cliffweng). The dojo is a road map for kids to learn the power of coding through Python. It provides a cohesive series of learning activities for learners to gain basic coding skills and appreciation for what coding can do.

## Overview & Road Map

This is a road map for kids to learn coding.

```
Scratch - Processing - Python  - Algorithm - USACO 
                               - Data pkgs - SODS - Kaggle - Research
                     - Node.js - React.js  - Hackthons - Start-up
```
- [Coding Dojo JS](https://cliffweng.github.io/coding-dojo-js/) - for kids to learn Javascrips.
- [Coding Dojo (Python)](https://cliffweng.github.io/coding-dojo/) - this site.
- [Scratch](https://scratch.mit.edu) - for kids k-5
- [Kaggle](https://www.kaggle.com/learn/overview) - to practice your ML skills with vast dataset.
- [USACO](https://usaco.guide/) - Computing Olympiad for high-schoolers.
- [Major League Hacking](https://mlh.io/) - for all the hackers out there.

## Getting Started

The TOC of this site is on the starting nodebook "Coding Dojo Overview".

The easiest way to get started is to use [Coding Dojo on Colab](https://colab.research.google.com/github/cliffweng/coding-dojo/blob/master/Coding_Dojo_Overview.ipynb). You don't need to install anything, everything is online.

For those more advanced kids who want to launch "Coding Dojo" locally, you need to have python and all the required packages installed. Just run `jupyter lab -ip 0.0.0.0` or `run.bat` once you downloaded it.

### Required Packages
- numpy
- pandas
- jupyter
- matplotlib
- scikit-learn
- streamlit
- nltk
- seaborn
- lxml
- html5lib
- bs4
### Build Environments

``` 
docker build -t coding_dojo .
```
Launch a container with the following command:
``` 
docker run -p 8888:8888 -p 8501:8501 --name codedojo -e GRANT_SUDO=yes --user root -e JUPYTER_ENABLE_LAB=yes -v %cd%:/home/jovyan coding_dojo
```

## Why Python
Python is the language od data. There are so much support for data science, machine learning and deep learning on Python. Python could be an excellent back-end tool that collect and compute the data and serves them through a web service.
## Other Python Learning Sources

- [W3Schools](https://w3schools.com/python/)
- [FreeCodeCamp](https://guide.freecodecamp.org/python)
- [Kaggle](https://www.kaggle.com/learn/overview)
- [TutorialsPoint](https://www.tutorialspoint.com/python/) 
