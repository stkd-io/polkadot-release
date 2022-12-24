FROM python:alpine3.15

ENV TZ=""
ENV PD_API_KEY=""
ENV SLACK_API=""
ENV SLACK_CHANNEL_NAME=""
ENV PYTHONUNBUFFERED=true


LABEL Maintainer="@frazzled_dazzle"
LABEL Company="stkd.io"

#Setup env
RUN apk update;\
    apk add py-pip;\
    apk add --no-cache tzdata

RUN pip install feedparser;\
    pip install datetime;\
    pip install time;\
    pip install sys;\
    pip install pathlib;\
    pip install pdpyras;\
    pip install os;\
    pip install slack_sdk;\
    pip install requests

#Patch the image
RUN apk upgrade

RUN mkdir /data;

COPY ./app/main.py /data/polka_alert.py

CMD [ "python", "/data/polka_alert.py"]

