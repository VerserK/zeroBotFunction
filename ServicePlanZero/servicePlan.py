import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def run():
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {'content-type': 'application/json','Authorization':'Bearer J9o+1YH2mYc/4RiFFOjgXTYqCIxT//ctqWgLjB4kyYlw8qaieSnNl42uyn/TMfk7PuWAe9S8hyL5JDIA00Vfr24Ltdq+97ds4BNk4htsAIRkiDDAVQ0PKiz2wreUTFBG4Vpv+hDtLSk1QAnu2V2pOwdB04t89/1O/w1cDnyilFU='}
    body = {
        "to": 'U97caf21a53b92919005e158b429c8c2b',
        "messages": [
            {
            "type":"text",
            "text":"Hello, user"
            },
            {
                "type":"text",
                "text":"May I help you?"
            }
        ]
    }
    r = requests.post(url, headers=headers, json=body)