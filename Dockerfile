FROM python:3.8-buster

RUN pip install h11 h2 hypercorn quart discord-py tinydb oauth2client gspread quart_cors

ADD app.py /
ADD config.ini /

ADD certs /certs
ADD library /library

RUN pip install quart discord-py tinydb oauth2client gspread sortedcontainers

CMD [ "python", "./app.py" ]
