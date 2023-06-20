FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install python=3.8
RUN pip install rdkit-pypi
RUN pip install scikit-learn==0.23.2
RUN pip install matplotlib==3.7
RUN pip install numpy==1.20.3
RUN pip install pandas==2.0.2
RUN pip install joblib

WORKDIR /repo
COPY . /repo 
