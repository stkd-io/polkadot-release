from curses import raw
import json
import feedparser
from datetime import datetime, timedelta
import sys
import os
from os import environ
import pdpyras
from slack_sdk import WebClient
import requests
import time
##########################
#
#       Variables
#
##########################
#Get the latest release
latest = 0

if environ.get('PD_API_KEY') is not None:
    #Service -> Custom Change Event Transformer key
    PD_API_KEY = os.environ['PD_API_KEY']

    #Setting Pager duty
    session = pdpyras.EventsAPISession(PD_API_KEY)

#Slack variables
if environ.get('SLACK_CHANNEL_NAME') is not None:
    SLACK_CHANNEL_NAME = os.environ['SLACK_CHANNEL_NAME']

if environ.get('SLACK_API') is not None:
    SLACK_API = os.environ['SLACK_API']

##########################
#
#       functions
#
##########################
def send_slack_message(api, channel_name, message):
    client = WebClient(api)
    response = client.chat_postMessage(
        channel=channel_name,
        text=message)

def sendAlert(message):
    sys.stdout.write(message)
    if environ.get('SLACK_API') is not None and environ.get('SLACK_CHANNEL_NAME') is not None:
        send_slack_message(SLACK_API, SLACK_CHANNEL_NAME, message)
    if 'rc' not in versionNumber[0]:
        if environ.get('PD_API_KEY') is not None:
            session.trigger(message, "polkadot")
    time.sleep(3600)


print("Starting...")
#Github page to monitor for releases
response = requests.get('https://github.com/paritytech/polkadot/releases.atom')
raw_atom = feedparser.parse(response.content)

#Parse the .atom
entries = raw_atom['entries']
published_time = entries[latest]['updated']
version = entries[latest]['title']
versionNumber = version.split(":")

#Check if released in the last hour
if (datetime.utcnow() - datetime.strptime(published_time, '%Y-%m-%dT%H:%M:%SZ')) > timedelta(hours=1):
    print("No New Release in the last hour, lastest release was: " + versionNumber[0])
    
else:
    #Check if version is a release canidate
    if 'rc' in versionNumber[0]:
        message = "Release Candidate: " + versionNumber[0] + " has been published\n" 
    #Version is a release
    else:
        message = "[!] New Release: " + versionNumber[0]
    sendAlert(message)

