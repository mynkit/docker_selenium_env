FROM joyzoursky/python-chromedriver:3.6

WORKDIR /src

COPY ./requirements.txt ./

RUN pip install -U pip && \
    pip install -r requirements.txt && \
    apt-get update && apt-get install vim curl -y
