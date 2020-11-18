FROM python:3.8-buster

RUN pip install h11 h2 hypercorn quart discord-py tinydb oauth2client quart_cors sortedcontainers pyjwt google-api-python-client google-auth-httplib2 google-auth-oauthlib

ADD app.py /
ADD config.ini /

ADD certs /certs
ADD library /library

CMD [ "python", "./app.py" ]
