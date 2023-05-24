import datetime
import requests
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd
import numpy as np

def callRow(sparepart,quantity):
    callRow = {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": str(sparepart),
                    "size": "sm",
                    "color": "#555555",
                    "flex": 5,
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": str(quantity),
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            }
    return callRow

def callTemplate(QRYADD):
    callTemplate= {
        "type": "box",
        "layout": "horizontal",
        "contents": [
        {
            "type": "text",
            "text": "ชื่ออะไหล่",
            "size": "md",
            "color": "#111111",
            "flex": 0,
            "weight": "bold"
        },
        {
            "type": "text",
            "text": "จำนวน",
            "size": "md",
            "color": "#111111",
            "align": "end",
            "weight": "bold"
        }
        ]
    },
    QRYADD
    {
        "type": "separator",
        "margin": "xxl"
    }
    return callTemplate

def unique(list1):
 
    # initialize a null list
    unique_list = []
    i = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        i.append(x)
    return i

def sendApi(UID,Data):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {'content-type': 'application/json','Authorization':'Bearer J9o+1YH2mYc/4RiFFOjgXTYqCIxT//ctqWgLjB4kyYlw8qaieSnNl42uyn/TMfk7PuWAe9S8hyL5JDIA00Vfr24Ltdq+97ds4BNk4htsAIRkiDDAVQ0PKiz2wreUTFBG4Vpv+hDtLSk1QAnu2V2pOwdB04t89/1O/w1cDnyilFU='}
    body = {
        "to": UID,
        # "to": "U97caf21a53b92919005e158b429c8c2b",
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
                                "text": "รายการอะไหล่ที่ต้องเปลี่ยน",
                                "weight": "bold",
                                "color": "#1DB446",
                                "size": "lg"
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "รายการอะไหล่",
                                        "flex": 0,
                                        "weight": "bold",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "จำนวน",
                                        "weight": "bold",
                                        "size": "sm",
                                        "align": "end"
                                    }
                                    ]
                                }
                                ],
                                "spacing": "sm",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": Data
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "ตรวจเช็คราคาอะไหล่",
                                "uri": "https://store.kasetinno.com/"
                                },
                                "style": "primary"
                            }
                            ]
                        },
                        "styles": {
                            "footer": {
                            "separator": True
                            }
                        }
                        }
            }
        ]
    }
    r = requests.post(url, headers=headers, json=body)

laborvalue = 'DC-70G PLUS'.split(' ')
j1 = ''.join(laborvalue[0])
print (j1)
today = datetime.datetime.now()
todayTostr = today.strftime('%m%d%Y%H%M%S')
print(todayTostr)

datetime_obj = datetime.datetime.now()
timedel = datetime.timedelta(days=7)
datetime_obj = datetime_obj + timedel
datequeryStr = datetime_obj.strftime("%Y-%m-%d")

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
                ",[VIN]"
                ",[Labor Value Main Type]"
            "FROM [ZEROSearchDB].[dbo].[Service_Plan]" 
            # "WHERE [Next Service Date] = '" + datequeryStr + "'"
            "WHERE [Next Service Date] = '2019-06-30'"
        )
resultsetloc = conn.execute(query)
results_as_dict_loc = resultsetloc.mappings().all()
df = pd.DataFrame(results_as_dict_loc)

for index, row in df.iterrows():
    ### Query Check User ###
    qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model] FROM [Line Data].[dbo].[Profile Line] PL "
                "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                "WHERE IAC.[VIN] = '"+ row['VIN'] +"'"
                "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                )
    resultsetCheck = conn.execute(qry)
    results_as_dict_Check = resultsetCheck.mappings().all()
    df1 = pd.DataFrame(results_as_dict_Check)
    for x,i in df1.iterrows():
        UID = 'U97caf21a53b92919005e158b429c8c2b'
        if i['Product Type'] == 'TRACTOR':
            laborvalue = row['Labor Value Main Type']
            laborvalue = laborvalue.split(' ')
            lv = ''.join(laborvalue[0])
            master = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1250,1300,1400,1500,1600,1700,1750,1800,1900,2000]
            if row['Counter for Next Service'] in master:
                print(row['Counter for Next Service'])
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                    "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                    "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df3 = pd.DataFrame(results_as_dict_Check)
                qrydf3 = []
                for a,b in df3.iterrows():
                    qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                sendApi(UID,qrydf3)
            else:
                NextService = row['Counter for Next Service']
                print(NextService)
                oper = []
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                    "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df4 = pd.DataFrame(results_as_dict_Check)
                oper = df4['ชั่วโมงต่อไป'].str.strip('.ทุกชม ปี')
                out = oper.to_numpy().tolist()
                newOut = unique(out)
                newOut.remove(None)
                newOut.remove('2')
                print(newOut)
                qrydf3 = []
                for i in newOut:
                    conditionService = NextService % int(i)
                    if conditionService == 0:
                        qry = sa.text("SELECT *"
                            "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                            "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                            "AND (["+ i + "] <> '0')"
                        )
                        resultsetCheck = conn.execute(qry)
                        results_as_dict_Check = resultsetCheck.mappings().all()
                        df3 = pd.DataFrame(results_as_dict_Check)
                        for a,b in df3.iterrows():
                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                            qrydf3 = unique(qrydf3)
                        sendApi(UID,qrydf3)
        elif i['Product Type'] == 'MINI EXCAVATOR':
            laborvalue = row['Labor Value Main Type']
            laborvalue = laborvalue.split(' ')
            lv = ''.join(laborvalue[0])
            master = [50,100,250,500,750,1000,1250,1500,1750,2000]
            if row['Counter for Next Service'] in master:
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                    "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                    "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df3 = pd.DataFrame(results_as_dict_Check)
                qrydf3 = []
                for a,b in df3.iterrows():
                    qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                print(qrydf3)
                sendApi(UID,qrydf3)
            else:
                NextService = row['Counter for Next Service']
                oper = []
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                    "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df4 = pd.DataFrame(results_as_dict_Check)
                oper = df4['ชั่วโมงต่อไป'].str.strip('.ทุกชม ปีๆชั่วโมง')
                out = oper.to_numpy().tolist()
                newOut = unique(out)
                newOut.remove(None)
                newOut.remove('2')
                qrydf3 = []
                for i in newOut:
                    if i == 20002:
                        i = 2000
                        conditionService = NextService % int(i)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                                "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                "AND (["+ i + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)
                    else:
                        conditionService = NextService % int(i)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                                "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                "AND (["+ i + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)
        elif i['Product Type'] == 'RICE TRANSPLANTER':
            print('RICE TRANSPLANTER')
            laborvalue = row['Labor Value Main Type']
            laborvalue = laborvalue.split(' ')
            lv = ''.join(laborvalue[0])
            master = [20,30,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000]
            if row['Counter for Next Service'] in master:
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Rice]"
                    "WHERE [สินค้า] LIKE '"+ lv +"'"
                    "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df3 = pd.DataFrame(results_as_dict_Check)
                qrydf3 = []
                for a,b in df3.iterrows():
                    qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                sendApi(UID,qrydf3)
            else:
                NextService = row['Counter for Next Service']
                oper = []
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Rice]"
                    "WHERE [สินค้า] LIKE '"+ lv +"%'"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df4 = pd.DataFrame(results_as_dict_Check)
                oper = df4['ชั่วโมงต่อไป'].str.strip('.ทุกชม ปีๆชั่วโมง')
                out = oper.to_numpy().tolist()
                newOut = unique(out)
                newOut.remove(None)
                newOut.remove('2')
                qrydf3 = []
                for m in newOut:
                    if m == 8002:
                        m = 800
                        conditionService = NextService % int(m)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Rice]"
                                "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                "AND (["+ m + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)
                    else:
                        conditionService = NextService % int(m)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Rice]"
                                "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                "AND (["+ m + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)
        elif i['Product Type'] == 'COMBINE HARVESTER':
            laborvalue = row['Labor Value Main Type']
            laborvalue = laborvalue.split(' ')
            lv = ''.join(laborvalue[0])
            master = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000]
            if row['Counter for Next Service'] in master:
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                    "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                    "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df3 = pd.DataFrame(results_as_dict_Check)
                qrydf3 = []
                for a,b in df3.iterrows():
                    qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                sendApi(UID,qrydf3)
            else:
                NextService = row['Counter for Next Service']
                oper = []
                qry = sa.text("SELECT *"
                    "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                    "WHERE [สินค้า] LIKE '"+ lv +"%'"
                )
                resultsetCheck = conn.execute(qry)
                results_as_dict_Check = resultsetCheck.mappings().all()
                df4 = pd.DataFrame(results_as_dict_Check)
                oper = df4['ชั่วโมงต่อไป'].str.strip('.ทุกชม ปีๆชั่วโมง')
                out = oper.to_numpy().tolist()
                newOut = unique(out)
                newOut.remove(None)
                newOut.remove('2')
                qrydf3 = []
                for i in newOut:
                    if i == 8002:
                        i = 800
                        conditionService = NextService % int(i)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                                "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                "AND (["+ i + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)
                    else:
                        conditionService = NextService % int(i)
                        if conditionService == 0:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                                "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                "AND (["+ i + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            for a,b in df3.iterrows():
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                                qrydf3 = unique(qrydf3)
                            sendApi(UID,qrydf3)