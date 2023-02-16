import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def run():
    ### Connect DB ####
    server = 'skcdwhprdmi.siamkubota.co.th'
    database =  'KIS Data'
    username = 'skcadminuser'
    password = 'DEE@skcdwhtocloud2022prd'
    driver = '{ODBC Driver 17 for SQL Server}'
    dsn = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    params = urllib.parse.quote_plus(dsn)
    engine = sa.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
    conn = engine.connect()

    query = sa.text('''SELECT TOP (1000) [IOBJGUID]
                    ,[Service Type]
                    ,[Material Number]
                    ,[Next Service Date]
                    ,[Counter for Next Service]
                    ,[Unit of Counter for Next Service]
                    ,[Valid From (Time Stamp)]
                    ,[Valid To (Time Stamp)]
                    ,[Date of Last Change]
                    ,[Status]
                    ,[Request Date]
                    ,[Approve Date]
                    ,[Closed]
                    ,[DBM Order Number]
                    ,[Billing date for billing index and printout]
                    ,[Customer]
                    ,[Vehicle Identification Number (Vehicle Identification No.)]
                    ,[Vehicle Sales Organization]
                    ,[Sales Date]
                    ,[Labor Value Main Type]
                    ,[Engine Code]
                FROM [ZEROSearchDB].[dbo].[Service_Plan] WHERE [Vehicle Identification Number (Vehicle Identification No.)] = 'KBCCZ494VM3F30232'
            '''
            )
    resultsetloc = conn.execute(query)
    results_as_dict_loc = resultsetloc.mappings().all()

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