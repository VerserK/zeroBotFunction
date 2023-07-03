import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def cellLoc(VIN):
    datetime_obj = datetime.datetime.now()
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")

    ### Connect DB ####
    server = 'skcdwhprdmi.siamkubota.co.th'
    database =  'master'
    username = 'skcadminuser'
    password = 'DEE@skcdwhtocloud2022prd'
    driver = '{ODBC Driver 17 for SQL Server}'

    dsn = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    params = urllib.parse.quote_plus(dsn)
    engine = sa.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
    conn = engine.connect()

    query = sa.text("SELECT [LastUpdate]"
            ",[EquipmentName]"
            ",[SubDistrict]"
            ",[District]"
            ",[Province]"
            ",[Country]"
            ",[Hour]"
            ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '" + datequeryStr + "' AND [EquipmentName] = '" + VIN + "'"
            # ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '2023-02-13' AND [EquipmentName] = '" + VIN + "'"
            " AND [SubDistrict] <> '' AND [District] <> '' AND [Province] <> '' AND [Country] <> '' AND [Hour] > 0"
            )
    resultsetloc = conn.execute(query)
    results_as_dict_loc = resultsetloc.mappings().all()
    dfLoc = pd.DataFrame(results_as_dict_loc)
    locloop=[]
    num = 0
    for index, row in dfLoc.iterrows():
        num += 1
        try:
            listHour = str(row['Hour']).split('.')
            if listHour[0] == '0':
                Hour = listHour[1]+' นาที'
            else :
                Hour = listHour[0]+' ชม. '+listHour[1]+' นาที'
        except:
            Hour = str(row['Hour'])+' ชม.'
        address={
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "text",
                        "text": "จุดที่ ("+str(num)+") :",
                        "wrap": True,
                        "color": "#818181"
                    },
                    {
                        "type": "text",
                        "text": 'ต.'+ str(row['SubDistrict']) + ' อ.' + str(row['District']) + ' จ.' + str(row['Province']) + ' ' + str(row['Country']) + ' \n(' + str(Hour) +')',
                        "wrap": True
                    }
                ]
            }
        locloop.append(address)
    return locloop

def main():
    true = True
    datetime_obj = datetime.datetime.now()
    datetimeThai = thai_strftime(datetime_obj, "%A %d %B %Y")
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")

    ### Connect DB ####
    server = 'skcdwhprdmi.siamkubota.co.th'
    database =  'master'
    username = 'skcadminuser'
    password = 'DEE@skcdwhtocloud2022prd'
    driver = '{ODBC Driver 17 for SQL Server}'

    dsn = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    params = urllib.parse.quote_plus(dsn)
    engine = sa.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)
    conn = engine.connect()

    ### Query Notnull ###
    query = sa.text("SELECT [LastUpdate]"
                ",[EquipmentName]"
                ",[SubDistrict]"
                ",[District]"
                ",[Province]"
                ",[Country]"
                ",[Hour]"
                ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '" + datequeryStr + "'"
                # ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '2023-02-21'"
                " AND [SubDistrict] <> '' AND [District] <> '' AND [Province] <> '' AND [Country] <> '' AND [Hour] > 0"
                " AND [Rank] = 1"
                )
    resultsetnotnull = conn.execute(query)
    results_as_dict_notnull = resultsetnotnull.mappings().all()
    df = pd.DataFrame(results_as_dict_notnull)

    ### Query Check User ###
    qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model], MC.[Name] AS McName FROM [Line Data].[dbo].[Profile Line] PL "
                "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                "LEFT JOIN [Line Data].[dbo].[MC Name] MC ON IAC.[VIN] = MC.[VIN]"
                "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                )
    resultset = conn.execute(qry)
    results_as_dict = resultset.mappings().all()
    df1 = pd.DataFrame(results_as_dict)
    dfFinal = df.merge(df1, left_on='EquipmentName', right_on='VIN')
    dfFinal = dfFinal.sort_values(by=['UserId'])
    for index, row in dfFinal.iterrows():
        ProductType = row['Product Type']
        if ProductType == 'TRACTOR':
            ProductType = 'รถแทรกเตอร์'
        elif ProductType == 'MINI EXCAVATOR':
            ProductType = 'รถขุด'
        elif ProductType == 'RICE TRANSPLANTER':
            ProductType = 'รถดำนา'
        elif ProductType == 'COMBINE HARVESTER':
            ProductType = 'รถเกี่ยวนวดข้าว'
        
        if row['McName'] == None:
            McName = '-'
        else :
            McName = row['McName']
        url = 'https://api.line.me/v2/bot/message/push'
        headers = {'content-type': 'application/json','Authorization':'Bearer J9o+1YH2mYc/4RiFFOjgXTYqCIxT//ctqWgLjB4kyYlw8qaieSnNl42uyn/TMfk7PuWAe9S8hyL5JDIA00Vfr24Ltdq+97ds4BNk4htsAIRkiDDAVQ0PKiz2wreUTFBG4Vpv+hDtLSk1QAnu2V2pOwdB04t89/1O/w1cDnyilFU='}
        body = {
        "to": row['UserId'],
        "messages": [
            {
            "type": "flex",
            "altText": "Daily Report",
            "contents": {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81o_m4U7QHtGj2Kcbfky94KRBOoa8-ahtpmsD75fO4FUU5S2mPfirReb-Es939EKEL3i9BTSWGFgXZhZegSy45kV_u-b=s2560"
                    },
                    {
                        "type": "text",
                        "text": "สรุปการทำงานประจำวัน",
                        "size": "xl",
                        "weight": "bold",
                        "color": "#ffffff",
                        "margin": "sm"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": datetimeThai,
                        "color": "#ffffff",
                        "size": "md",
                        "flex": 4,
                        "weight": "bold",
                        "wrap": true
                    }
                    ]
                }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#F25822",
                "spacing": "md",
                "height": "96px",
                "paddingTop": "22px",
                "background": {
                "type": "linearGradient",
                "angle": "12deg",
                "startColor": "#F25822",
                "endColor": "#FDB777",
                "centerColor": "#FD7F2C"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81oCBsV9bpCziqunhs12VWwNDqcbl0bOgS4g8lW8_A7ZsJg-agKguPAiQuVVMNTvxUA0qA-t0zwAWmW3wyC3Ul-0B1oDvQ=s2560"
                    },
                    {
                        "type": "text",
                        "text": "ข้อมูลรถของคุณ",
                        "weight": "bold",
                        "decoration": "underline",
                        "margin": "sm"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่อรถ :",
                            "color": "#818181",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": McName
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ประเภทรถ :",
                            "color": "#818181",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": ProductType,
                            "wrap": true
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "หมายเลขรถ :",
                            "color": "#818181",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": row['VIN'],
                            "wrap": true
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "รุ่น :",
                            "color": "#818181",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": row['Model'],
                            "wrap": true
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "sm"
                    }
                    ],
                    "spacing": "sm"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81oF0sakxdLuRxBQAAjdZhfEEYrnnQvCDi3kwaEW6hDJmQHDSjnVLVoAyGKGMpgDGIgCw4RCUMlrV67HE7KnYGkh6mF9qA=s2560",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "สถานที่ทำงาน",
                        "weight": "bold",
                        "decoration": "underline",
                        "wrap": true
                    }
                    ],
                    "spacing": "sm",
                    "margin": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": cellLoc(row['VIN']),
                    "spacing": "sm"
                }
                ]
            }
            }
            }
        ]
    }
        r = requests.post(url, headers=headers, json=body)
