FROM python:latest

ADD app.py /
ADD config.ini /

ADD certs /certs
ADD library /library

RUN pip install quart discord-py tinydb oauth2client gspread

CMD [ "python", "./app.py" ]
