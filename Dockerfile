ARG BASE_CONTAINER=jupyter/base-notebook:python-3.8.6
FROM $BASE_CONTAINER
USER root
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
USER $NB_UID