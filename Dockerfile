FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge numpy=1.20.3
RUN conda install -c conda-forge scikit-learn=0.23.2
RUN pip install rdkit==2022.3.5
RUN pip install matplotlib==3.7
RUN pip install pandas==2.0.2
RUN pip install joblib==1.3.0

WORKDIR /repo
COPY . /repo 
