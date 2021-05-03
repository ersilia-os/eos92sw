FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit
RUN pip install scikit-learn==0.23
RUN pip install pandas
RUN pip install joblib

WORKDIR /repo
COPY . /repo
