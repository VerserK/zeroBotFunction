import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def cellLoc(VIN):
    datetime_obj = datetime.datetime.now()
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")
    # datequeryStr = '2021-01-12'

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
            # ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '2023-12-07' AND [EquipmentName] = 'KBCDZ552PP3D70009'"
            # " AND [SubDistrict] <> '' AND [District] <> '' AND [Province] <> '' AND [Country] <> '' AND [Hour] > 0"
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
                int_list = float('.'+listHour[1])
                hourMin = str(int_list*60).split('.')
                Hour = hourMin[0] +' นาที'
            else :
                int_list = float('.'+listHour[1])
                hourMin = str(int_list*60).split('.')
                Hour = listHour[0]+' ชั่วโมง '+hourMin[0]+' นาที'
        except:
            Hour = str(row['Hour'])+' ชั่วโมง'
        if row['Country'] == None:
            address = {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "วันนี้รถของคุณไม่ได้ทำงาน",
                            "contents": []
                        }
                        ]
                    }
            locloop.append(address)
            print('IF')
            print(locloop)
        else:
            address = {
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
                            "text": 'ต.'+ str(row['SubDistrict']) + ' อ.' + str(row['District']) + ' จ.' + str(row['Province']) + '\n(' + str(Hour) +')',
                            # "text": 'ต.'+ str(row['SubDistrict']) + ' อ.' + str(row['District']) + ' จ.' + str(row['Province']),
                            "wrap": True
                        }
                    ]
                }
            locloop.append(address)
            print('Else')
            print(locloop)
    return locloop

def main():
    true = True
    datetime_obj = datetime.datetime.now()
    datetimeThai = thai_strftime(datetime_obj, "%A %d %B %Y")
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")
    Linetoken = 'HvSWl3gV8+hLK5/2xb8Fejzg5QxJRdvtZiHf5irm0RiMpD6h1Owlj15XpwdHX6bVbXtfktmgXCEc0WmYzk/i8lKxNNCRnmo78QPupI9CVqvUTPaPtrbETMzLZcE+AKiEBK4CP7BzcE9Y2jy1YEDjRwdB04t89/1O/w1cDnyilFU='
    # datequeryStr = '2024-03-25'

    ### Connect DB ####
    server = 'skcdwhprdmi.siamkubota.co.th'
    database = 'KIS Data'
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
                # ",[Rank] FROM [KIS Data].[dbo].[Engine_Location_Agg] WHERE [LastUpdate] = '2023-12-07'"
                # " AND [SubDistrict] <> '' AND [District] <> '' AND [Province] <> '' AND [Country] <> '' AND [Hour] > 0"
                # " AND [Rank] = 1"
                )
    resultsetnotnull = conn.execute(query)
    results_as_dict_notnull = resultsetnotnull.mappings().all()
    df = pd.DataFrame(results_as_dict_notnull)
    print(df)

    ### Query Check User ###
    qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model], MC.[Name] AS McName FROM [Line Data].[dbo].[Profile Line] PL "
                "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                "LEFT JOIN [Line Data].[dbo].[MC Name] MC ON IAC.[VIN] = MC.[VIN]"
                "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                )
    resultset = conn.execute(qry)
    results_as_dict = resultset.mappings().all()
    df1 = pd.DataFrame(results_as_dict)
    print(df1)

    dfFinal = df.merge(df1, left_on='EquipmentName', right_on='VIN')
    dfFinal = dfFinal.drop_duplicates(subset=['VIN'], keep='last')
    dfFinal = dfFinal.sort_values(by=['UserId'])
    print(dfFinal)
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
        headers = {'content-type': 'application/json','Authorization':'Bearer ' + Linetoken}
        print(row['UserId'])
        body = {
        "to": row['UserId'],
        # "to": 'U6033cf390924547c3a509fc418b7a0db',
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
                        "url": "https://dwhwebstorage.blob.core.windows.net/pic/calendar.png"
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
                        "url": "https://dwhwebstorage.blob.core.windows.net/pic/180527_kubota-Icon-07.png"
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
                        "url": "https://dwhwebstorage.blob.core.windows.net/pic/placeholder.png",
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
        exit()

main()