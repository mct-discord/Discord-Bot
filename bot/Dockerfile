FROM python:3.8-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD app.py /
ADD config.ini /

ADD certs /certs
ADD library /library

CMD [ "python", "./app.py" ]
