import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def run():
    datetime_obj = datetime.datetime.now()
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")
    # datequeryStr = '2023-01-15'

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

    query = sa.text("SELECT"
                    "[Next Service Date]"
                    ",[Counter for Next Service]"
                    ",[Vehicle Identification Number (Vehicle Identification No.)]"
                    ",[Labor Value Main Type]"
                "FROM [ZEROSearchDB].[dbo].[Service_Plan]" 
                "WHERE [Next Service Date] = '" + datequeryStr + "'"
            )
    resultsetloc = conn.execute(query)
    results_as_dict_loc = resultsetloc.mappings().all()
    df = pd.DataFrame(results_as_dict_loc)

    for index, row in df.iterrows():
        ### Query Check User ###
        qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model] FROM [Line Data].[dbo].[Profile Line] PL "
                    "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                    "WHERE IAC.[VIN] = '"+ row['Vehicle Identification Number (Vehicle Identification No.)'] +"'"
                    "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                    )
        resultsetCheck = conn.execute(qry)
        results_as_dict_Check = resultsetCheck.mappings().all()
        
        df1 = pd.DataFrame(results_as_dict_Check)
        for x,i in df1.iterrows():
            ProductType = i['Product Type']
            if ProductType == 'TRACTOR':
                ProductType = 'รถแทรกเตอร์'
            elif ProductType == 'MINI EXCAVATOR':
                ProductType = 'รถขุด'
            elif ProductType == 'RICE TRANSPLANTER':
                ProductType = 'รถดำนา'
            elif ProductType == 'COMBINE HARVESTER':
                ProductType = 'รถเกี่ยวนวดข้าว'
            nextservicedate = thai_strftime(row['Next Service Date'],"%d-%m-%Y")
            url = 'https://api.line.me/v2/bot/message/push'
            headers = {'content-type': 'application/json','Authorization':'Bearer J9o+1YH2mYc/4RiFFOjgXTYqCIxT//ctqWgLjB4kyYlw8qaieSnNl42uyn/TMfk7PuWAe9S8hyL5JDIA00Vfr24Ltdq+97ds4BNk4htsAIRkiDDAVQ0PKiz2wreUTFBG4Vpv+hDtLSk1QAnu2V2pOwdB04t89/1O/w1cDnyilFU='}
            body = {
                "to": i['UserId'],
                "messages": [
                    {
                        "type": "flex",
                        "altText": "Service Plan Report",
                        "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "แจ้งเตือนจากระบบ !!",
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "text",
                            "text": "รถของคุณครบกำหนดตรวจเช็กระยะแล้ว",
                            "align": "center",
                            "size": "xs"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "ผลิตภัณฑ์",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": ProductType,
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "หมายเลขรถ",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": row['Vehicle Identification Number (Vehicle Identification No.)'],
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "รุ่น",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": row['Labor Value Main Type'],
                                    "flex": 5,
                                    "color": "#666666",
                                    "size": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "ชั่วโมงรถ",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": str(row['Counter for Next Service']),
                                    "flex": 5,
                                    "color": "#666666",
                                    "size": "sm",
                                    "wrap": True
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "วันที่ครบกำหนด",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 3
                                },
                                {
                                    "type": "text",
                                    "text": nextservicedate,
                                    "flex": 5,
                                    "color": "#666666",
                                    "size": "sm",
                                    "wrap": True
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "กรุณากินข้าวให้ตรงเวลา",
                                "size": "sm",
                                "wrap": True,
                                "align": "center"
                            }
                            ],
                            "margin": "md"
                        }
                        ]
                    }
                    }
                    }
                ]
            }
            r = requests.post(url, headers=headers, json=body)