import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd
from datetime import datetime, date, timedelta

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

def sendApi(UID,Data,sumAll):
    true = True
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {'content-type': 'application/json','Authorization':'Bearer HvSWl3gV8+hLK5/2xb8Fejzg5QxJRdvtZiHf5irm0RiMpD6h1Owlj15XpwdHX6bVbXtfktmgXCEc0WmYzk/i8lKxNNCRnmo78QPupI9CVqvUTPaPtrbETMzLZcE+AKiEBK4CP7BzcE9Y2jy1YEDjRwdB04t89/1O/w1cDnyilFU='}
    body = {
        "to": UID,
        # "to": "U97caf21a53b92919005e158b429c8c2b",
        "messages": [
            {
                "type": "flex",
                "altText": "Service Plan Report",
                "contents": {
                        "type": "bubble",
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
                                    "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81rsJvgMIyi67izNEVIzhpelG1b9T-dqAvt1_Gr0rrJACWxIjiYTcfYi_DobAUIcF7nSs0zz2s9nRsio-tCdo6cUvEd5IA=s2560"
                                },
                                {
                                    "type": "text",
                                    "text": "รายการอะไหล่ที่เปลี่ยน",
                                    "size": "xl",
                                    "weight": "bold",
                                    "color": "#ffffff",
                                    "margin": "sm",
                                    "wrap": true,
                                    "align": "start",
                                    "gravity": "center"
                                }
                                ]
                            }
                            ],
                            "paddingAll": "20px",
                            "backgroundColor": "#F25822",
                            "spacing": "md",
                            "height": "74px",
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
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "อะไหล่",
                                        "flex": 0,
                                        "weight": "bold",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "จำนวน",
                                        "weight": "bold",
                                        "size": "md",
                                        "align": "end"
                                    }
                                    ]
                                }
                                ],
                                "spacing": "sm",
                                "margin": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "sm",
                                "spacing": "sm",
                                "contents": Data
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "รวม",
                                    "size": "sm",
                                    "color": "#555555",
                                    "flex": 5,
                                    "wrap": True,
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": str(sumAll),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end",
                                    "weight": "bold"
                                }
                                ],
                                "margin": "lg"
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "เช็กราคาอะไหล่ คลิก!!",
                                "uri": "https://store.kasetinno.com/"
                                },
                                "style": "primary",
                                "color": "#F25822"
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
    return r

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

def run():
    true = True
    datetime_obj = datetime.now()
    timedel = timedelta(days=7)
    datetime_obj = datetime_obj + timedel
    datequeryStr = datetime_obj.strftime("%Y-%m-%d")
    Linetoken = 'HvSWl3gV8+hLK5/2xb8Fejzg5QxJRdvtZiHf5irm0RiMpD6h1Owlj15XpwdHX6bVbXtfktmgXCEc0WmYzk/i8lKxNNCRnmo78QPupI9CVqvUTPaPtrbETMzLZcE+AKiEBK4CP7BzcE9Y2jy1YEDjRwdB04t89/1O/w1cDnyilFU='
    # Test Date
    # datequeryStr = '2023-07-17'

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

    qryCheckKISonVIN = sa.text("SELECT [EPC].[VIN],[EPC].[Next Date] "
                                "FROM [Service Data].[dbo].[Service_Plan] SP "
                                "INNER JOIN [KIS Data].[dbo].[Engine_Periodical_Check] EPC ON [EPC].[VIN] = [SP].[VIN]"
                                "WHERE [EPC].[Next Date] = '" + datequeryStr + "'"
                                )
    resultvinkis = conn.execute(qryCheckKISonVIN)
    resultvinkis_as_dict_loc = resultvinkis.mappings().all()
    dfVinkis = pd.DataFrame(resultvinkis_as_dict_loc)
    print(dfVinkis)
    if len(dfVinkis) != 0:
        query = sa.text("SELECT DISTINCT "
                        "[EPC].[VIN] "
                        ",[Next Hours] as [Counter for Next Service] "
                        ",[LV Main Type] "
                        ",[Next Date] as [Plan Date] "
                    "FROM [KIS Data].[dbo].[Engine_Periodical_Check] EPC "
                    "INNER JOIN [Service Data].[dbo].[Service_Plan] SP ON [SP].[VIN] = [EPC].[VIN] " 
                    "WHERE [EPC].[Next Date] = '" + datequeryStr + "'"
                )
        resultsetloc = conn.execute(query)
        results_as_dict_loc = resultsetloc.mappings().all()
        df = pd.DataFrame(results_as_dict_loc)

        for index, row in df.iterrows():
            ### Query Check User ###
            qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model], MC.[Name] AS McName FROM [Line Data].[dbo].[Profile Line] PL "
                        "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                        "LEFT JOIN [Line Data].[dbo].[MC Name] MC ON IAC.[VIN] = MC.[VIN]"
                        "WHERE IAC.[VIN] = '"+ row['VIN'] +"'"
                        "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                        )
            resultsetCheck = conn.execute(qry)
            results_as_dict_Check = resultsetCheck.mappings().all()
            
            df1 = pd.DataFrame(results_as_dict_Check)

            queryCheckKis = sa.text("SELECT [Equipment_Name] FROM [KIS Data].[dbo].[Engine_Detail] "
                        "WHERE [Equipment_Name] = '"+ row['VIN'] +"'"
                        "ORDER BY [Equipment_Name] OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
                        )
            checkKis = conn.execute(queryCheckKis)
            checkKis_as_dict = checkKis.mappings().all()
                
            for x,i in df1.iterrows():
                UID = i['UserId']
                # UID = 'U97caf21a53b92919005e158b429c8c2b'
                ProductType = i['Product Type']
                if ProductType == 'TRACTOR':
                    ProductType = 'รถแทรกเตอร์'
                elif ProductType == 'MINI EXCAVATOR':
                    ProductType = 'รถขุด'
                elif ProductType == 'RICE TRANSPLANTER':
                    ProductType = 'รถดำนา'
                elif ProductType == 'COMBINE HARVESTER':
                    ProductType = 'รถเกี่ยวนวดข้าว'
                nextservicedate = thai_strftime(row['Plan Date'],"%d %B %Y")
                if i['McName'] == None:
                    McName = '-'
                else :
                    McName = i['McName']
                queryKIS = sa.text("SELECT *"
                            "FROM [KIS Data].[dbo].[Engine_Hours_Record]"
                            "WHERE [Equipment_Name] = '" + row['VIN'] + "'"
                            "ORDER BY [LastUpdate] Desc OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
                            )
                CheckKIS = conn.execute(queryKIS)
                dict_Check_KIS = CheckKIS.mappings().all()
                dfCheckKIS = pd.DataFrame(dict_Check_KIS)
                if len(dfCheckKIS) > 0:
                    for kisindex,kisloc in dfCheckKIS.iterrows():
                        try:
                            listHour = str(kisloc['Hours']).split('.')
                            CountHourKISStr = listHour[0]
                            CountHourKIS = ('{:,}'.format(int(CountHourKISStr)))+' ชั่วโมง'
                        # if listHour[0] == '0':
                        #     CountHourKIS = listHour[1]+' นาที'
                        # else :
                        #     CountHourKISStr = listHour[0]
                        #     print(CountHourKISStr)
                        #     CountHourKIS = ('{:,}'.format(int(CountHourKISStr)))+' ชั่วโมง '+listHour[1]+' นาที' 
                            # if listHour[0] == '0':
                            #     CountHourKIS = listHour[1]+' นาที'
                            # else :
                            #     CountHourKISStr = listHour[0]
                            #     print(CountHourKISStr)
                            #     CountHourKIS = ('{:,}'.format(int(CountHourKISStr)))+' ชั่วโมง '+listHour[1]+' นาที'   
                        except:     
                            CountHourKIS = ('{:,}'.format(str(kisloc['Hours'])))+' ชั่วโมง'       
                else:
                    CountHourKIS = ('{:,}'.format(int(row['Counter for Next Service'])))+' ชั่วโมง'
                countfornextserviceStr = ('{:,}'.format(int(row['Counter for Next Service'])))
                url = 'https://api.line.me/v2/bot/message/push'
                headers = {'content-type': 'application/json','Authorization':'Bearer ' + Linetoken}
                body = {
                    "to": i['UserId'],
                    "messages": [
                        {
                            "type": "flex",
                            "altText": "Service Plan Report",
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
                                            "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81qj794U-Poic5psPYYoUfWqGJ9ZkvYj-05hfgCv_UZvGhn-NZ5uc9Q45tFluUELjZYcHw6bfz96w1gNi4TB9ASVUKzSSQ=s2560"
                                        },
                                        {
                                            "type": "text",
                                            "text": "แจ้งเตือนจากระบบ",
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
                                            "text": "รถของคุณใกล้ถึงรอบตรวจเช็กเปลี่ยนถ่ายแล้ว",
                                            "color": "#ffffff",
                                            "size": "sm",
                                            "flex": 4,
                                            "weight": "regular",
                                            "wrap": true
                                        }
                                        ]
                                    }
                                    ],
                                    "paddingAll": "20px",
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
                                                "text": row['LV Main Type'],
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
                                                "text": "ชั่วโมงรถปัจจุบัน :",
                                                "color": "#818181",
                                                "wrap": true
                                            },
                                            {
                                                "type": "text",
                                                "text": CountHourKIS,
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
                                            "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81quzwMxVtBCTqCz6aNrSr0ZlVNMowQHyOHtla1M0p5MYow-cdvdfXpPvA-FoVbXvxdCWHa-uar2IMSTsx06p85Z_2Kt=s2560",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "รอบตรวจเช็กที่กำลังมาถึง",
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
                                        "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "รอบตรวจเช็กที่ :",
                                                "wrap": true,
                                                "color": "#818181"
                                            },
                                            {
                                                "type": "text",
                                                "text": countfornextserviceStr +' ชั่วโมง',
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
                                                "text": "วันที่ครบกำหนด :",
                                                "color": "#818181",
                                                "wrap": true
                                            },
                                            {
                                                "type": "text",
                                                "text": nextservicedate
                                            }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "สามารถนัดช่างออนไลน์ได้ด้วยตนเอง โดยคลิกที่ปุ่มด้านล่าง",
                                                "wrap": true
                                            }
                                            ],
                                            "margin": "md"
                                        }
                                        ],
                                        "spacing": "sm"
                                    }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "นัดช่างออนไลน์ คลิก !!",
                                        "uri": "https://korp.siamkubota.co.th/Customer/register.php?ln=U3bbdb6527df1f9c335ea672a6edb8149"
                                        },
                                        "style": "primary",
                                        "height": "md",
                                        "color": "#f25822"
                                    }
                                    ]
                                }
                            }
                        }
                    ]
                }
                r = requests.post(url, headers=headers, json=body)

                if len(checkKis_as_dict) == 0:
                    if i['Product Type'] == 'TRACTOR':
                        laborvalue = row['LV Main Type']
                        laborvalue = laborvalue.split(' ')
                        lv = ''.join(laborvalue[0])
                        master = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1250,1300,1400,1500,1600,1700,1750,1800,1900,2000]
                        if row['Counter for Next Service'] in master:
                            qry = sa.text("SELECT *"
                                "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                                "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                            )
                            resultsetCheck = conn.execute(qry)
                            results_as_dict_Check = resultsetCheck.mappings().all()
                            df3 = pd.DataFrame(results_as_dict_Check)
                            qrydf3 = []
                            sumAll = 0
                            for a,b in df3.iterrows():
                                sumAll += int(b['จำนวนชิ้น '])
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                            sendApi(UID,qrydf3,sumAll)
                        else:
                            NextService = row['Counter for Next Service']
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
                            for m in newOut:
                                conditionService = NextService % int(m)
                                if conditionService == 0:
                                    qry = sa.text("SELECT *"
                                        "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                                        "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                        "AND (["+ m + "] <> '0')"
                                    )
                                    resultsetCheck = conn.execute(qry)
                                    results_as_dict_Check = resultsetCheck.mappings().all()
                                    df3 = pd.DataFrame(results_as_dict_Check)
                                    sumAll = 0
                                    for a,b in df3.iterrows():
                                        sumAll += int(b['จำนวนชิ้น '])
                                        qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                                        qrydf3 = unique(qrydf3)
                                    sendApi(UID,qrydf3,sumAll)
                    elif i['Product Type'] == 'MINI EXCAVATOR':
                        print('MINI EXCAVATOR')
                        laborvalue = row['LV Main Type']
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
                            sumAll = 0
                            for a,b in df3.iterrows():
                                sumAll += int(b['จำนวนชิ้น'])
                                qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                            sendApi(UID,qrydf3,sumAll)
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
                            for m in newOut:
                                if m == 20002:
                                    m = 2000
                                    conditionService = NextService % int(m)
                                    if conditionService == 0:
                                        qry = sa.text("SELECT *"
                                            "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                                            "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                            "AND (["+ m + "] <> '0')"
                                        )
                                        resultsetCheck = conn.execute(qry)
                                        results_as_dict_Check = resultsetCheck.mappings().all()
                                        df3 = pd.DataFrame(results_as_dict_Check)
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
                                else:
                                    conditionService = NextService % int(m)
                                    if conditionService == 0:
                                        qry = sa.text("SELECT *"
                                            "FROM [ZEROSearchDB].[dbo].[Mt_Excavator]"
                                            "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                                            "AND (["+ m + "] <> '0')"
                                        )
                                        resultsetCheck = conn.execute(qry)
                                        results_as_dict_Check = resultsetCheck.mappings().all()
                                        df3 = pd.DataFrame(results_as_dict_Check)
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
                    elif i['Product Type'] == 'RICE TRANSPLANTER':
                        print('RICE TRANSPLANTER')
                        laborvalue = row['LV Main Type']
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
                            sumAll = 0
                            for a,b in df3.iterrows():
                                sumAll += int(b['จำนวนชิ้น '])
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                            sendApi(UID,qrydf3,sumAll)
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
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
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
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
                    elif i['Product Type'] == 'COMBINE HARVESTER':
                        laborvalue = row['LV Main Type']
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
                            sumAll = 0
                            for a,b in df3.iterrows():
                                sumAll += int(b['จำนวนชิ้น '])
                                qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                            sendApi(UID,qrydf3,sumAll)
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
                            for m in newOut:
                                if m == 8002:
                                    m = 800
                                    conditionService = NextService % int(m)
                                    if conditionService == 0:
                                        qry = sa.text("SELECT *"
                                            "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                                            "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                            "AND (["+ m + "] <> '0')"
                                        )
                                        resultsetCheck = conn.execute(qry)
                                        results_as_dict_Check = resultsetCheck.mappings().all()
                                        df3 = pd.DataFrame(results_as_dict_Check)
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
                                else:
                                    conditionService = NextService % int(m)
                                    if conditionService == 0:
                                        qry = sa.text("SELECT *"
                                            "FROM [ZEROSearchDB].[dbo].[Mt_Combine]"
                                            "WHERE [สินค้า] LIKE '"+ lv +"%'"
                                            "AND (["+ m + "] <> '0')"
                                        )
                                        resultsetCheck = conn.execute(qry)
                                        results_as_dict_Check = resultsetCheck.mappings().all()
                                        df3 = pd.DataFrame(results_as_dict_Check)
                                        sumAll = 0
                                        for a,b in df3.iterrows():
                                            sumAll += int(b['จำนวนชิ้น '])
                                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                                            qrydf3 = unique(qrydf3)
                                        sendApi(UID,qrydf3,sumAll)
                else :
                    print('IN KIS')
                    queryPeriodical = sa.text("SELECT [description (TH)],[Next Hours],[Next Date] FROM [KIS Data].[dbo].[Engine_Periodical_Check] "
                        "WHERE [VIN] = '" + row['VIN'] + "' AND [Next Date] = '" + datequeryStr + "'"
                        )
                    dataPeriodical = conn.execute(queryPeriodical)
                    dataPeriodical_as_dick = dataPeriodical.mappings().all()
                    print(len(dataPeriodical_as_dick))
                    sumAll = 0
                    if len(dataPeriodical_as_dick) > 0:
                        listCallRow = []
                        for item in dataPeriodical_as_dick:
                            sumAll += 1
                            listCallRow.append(callRow(item['description (TH)'],1))
                        print(listCallRow)
                        sendApi(UID,listCallRow, sumAll)
    
    query = sa.text("SELECT"
                    "[Plan Date] "
                    ",[Counter for Next Service] "
                    ",[VIN] "
                    ",[LV Main Type] "
                "FROM [Service Data].[dbo].[Service_Plan]" 
                "WHERE [LV Main Type] NOT LIKE '%KIS' AND [Plan Date] = '" + datequeryStr + "'"
                # "WHERE [Plan Date] = '2023-08-18'"
            )
    resultsetloc = conn.execute(query)
    results_as_dict_loc = resultsetloc.mappings().all()
    df = pd.DataFrame(results_as_dict_loc)

    for index, row in df.iterrows():
        ### Query Check User ###
        qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model], MC.[Name] AS McName FROM [Line Data].[dbo].[Profile Line] PL "
                    "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                    "LEFT JOIN [Line Data].[dbo].[MC Name] MC ON IAC.[VIN] = MC.[VIN]"
                    "WHERE IAC.[VIN] = '"+ row['VIN'] +"'"
                    "ORDER BY [UserId] OFFSET 0 ROWS FETCH NEXT 500 ROWS ONLY"
                    )
        resultsetCheck = conn.execute(qry)
        results_as_dict_Check = resultsetCheck.mappings().all()
        
        df1 = pd.DataFrame(results_as_dict_Check)

        queryCheckKis = sa.text("SELECT [Equipment_Name] FROM [KIS Data].[dbo].[Engine_Detail] "
                    "WHERE [Equipment_Name] = '"+ row['VIN'] +"'"
                    "ORDER BY [Equipment_Name] OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
                    )
        checkKis = conn.execute(queryCheckKis)
        checkKis_as_dict = checkKis.mappings().all()
            
        for x,i in df1.iterrows():
            UID = i['UserId']
            # UID = 'U97caf21a53b92919005e158b429c8c2b'
            ProductType = i['Product Type']
            if ProductType == 'TRACTOR':
                ProductType = 'รถแทรกเตอร์'
            elif ProductType == 'MINI EXCAVATOR':
                ProductType = 'รถขุด'
            elif ProductType == 'RICE TRANSPLANTER':
                ProductType = 'รถดำนา'
            elif ProductType == 'COMBINE HARVESTER':
                ProductType = 'รถเกี่ยวนวดข้าว'
            nextservicedate = thai_strftime(row['Plan Date'],"%d %B %Y")
            if i['McName'] == None:
                McName = '-'
            else :
                McName = i['McName']
            queryKIS = sa.text("SELECT *"
                        "FROM [KIS Data].[dbo].[Engine_Hours_Record]"
                        "WHERE [Equipment_Name] = '" + row['VIN'] + "'"
                        "ORDER BY [LastUpdate] Desc OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
                        )
            CheckKIS = conn.execute(queryKIS)
            dict_Check_KIS = CheckKIS.mappings().all()
            dfCheckKIS = pd.DataFrame(dict_Check_KIS)
            if len(dfCheckKIS) > 0:
                for kisindex,kisloc in dfCheckKIS.iterrows():
                    try:
                        listHour = str(kisloc['Hours']).split('.')
                        CountHourKISStr = listHour[0]
                        CountHourKIS = ('{:,}'.format(int(CountHourKISStr)))+' ชั่วโมง'
                        # if listHour[0] == '0':
                        #     CountHourKIS = listHour[1]+' นาที'
                        # else :
                        #     CountHourKISStr = listHour[0]
                        #     print(CountHourKISStr)
                        #     CountHourKIS = ('{:,}'.format(int(CountHourKISStr)))+' ชั่วโมง '+listHour[1]+' นาที'   
                    except:     
                        CountHourKIS = ('{:,}'.format(str(kisloc['Hours'])))+' ชั่วโมง'       
            else:
                CountHourKIS = ('{:,}'.format(int(row['Counter for Next Service'])))+' ชั่วโมง'
            
            countfornextserviceStr = ('{:,}'.format(int(row['Counter for Next Service'])))
            
            url = 'https://api.line.me/v2/bot/message/push'
            headers = {'content-type': 'application/json','Authorization':'Bearer ' + Linetoken}
            body = {
                "to": i['UserId'],
                "messages": [
                    {
                        "type": "flex",
                        "altText": "Service Plan Report",
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
                                        "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81qj794U-Poic5psPYYoUfWqGJ9ZkvYj-05hfgCv_UZvGhn-NZ5uc9Q45tFluUELjZYcHw6bfz96w1gNi4TB9ASVUKzSSQ=s2560"
                                    },
                                    {
                                        "type": "text",
                                        "text": "แจ้งเตือนจากระบบ",
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
                                        "text": "รถของคุณใกล้ถึงรอบตรวจเช็กเปลี่ยนถ่ายแล้ว",
                                        "color": "#ffffff",
                                        "size": "sm",
                                        "flex": 4,
                                        "weight": "regular",
                                        "wrap": true
                                    }
                                    ]
                                }
                                ],
                                "paddingAll": "20px",
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
                                            "text": row['LV Main Type'],
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
                                            "text": "ชั่วโมงรถปัจจุบัน :",
                                            "color": "#818181",
                                            "wrap": true
                                        },
                                        {
                                            "type": "text",
                                            "text": CountHourKIS,
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
                                        "url": "https://lh3.googleusercontent.com/drive-viewer/AFGJ81quzwMxVtBCTqCz6aNrSr0ZlVNMowQHyOHtla1M0p5MYow-cdvdfXpPvA-FoVbXvxdCWHa-uar2IMSTsx06p85Z_2Kt=s2560",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "รอบตรวจเช็กที่กำลังมาถึง",
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
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "รอบตรวจเช็กที่ :",
                                            "wrap": true,
                                            "color": "#818181"
                                        },
                                        {
                                            "type": "text",
                                            "text": countfornextserviceStr+' ชั่วโมง',
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
                                            "text": "วันที่ครบกำหนด :",
                                            "color": "#818181",
                                            "wrap": true
                                        },
                                        {
                                            "type": "text",
                                            "text": nextservicedate
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "สามารถนัดช่างออนไลน์ได้ด้วยตนเอง โดยคลิกที่ปุ่มด้านล่าง",
                                            "wrap": true
                                        }
                                        ],
                                        "margin": "md"
                                    }
                                    ],
                                    "spacing": "sm"
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "uri",
                                    "label": "นัดช่างออนไลน์ คลิก !!",
                                    "uri": "https://korp.siamkubota.co.th/Customer/register.php?ln=U3bbdb6527df1f9c335ea672a6edb8149"
                                    },
                                    "style": "primary",
                                    "height": "md",
                                    "color": "#f25822"
                                }
                                ]
                            }
                        }
                    }
                ]
            }
            r = requests.post(url, headers=headers, json=body)

            if len(checkKis_as_dict) == 0:
                if i['Product Type'] == 'TRACTOR':
                    laborvalue = row['LV Main Type']
                    laborvalue = laborvalue.split(' ')
                    lv = ''.join(laborvalue[0])
                    master = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1250,1300,1400,1500,1600,1700,1750,1800,1900,2000]
                    if row['Counter for Next Service'] in master:
                        qry = sa.text("SELECT *"
                            "FROM [ZEROSearchDB].[dbo].[Mt_Tractor]"
                            "WHERE [สินค้า] LIKE '"+ lv[:5] +"%'"
                            "AND (["+ str(row['Counter for Next Service']) + "] <> '0')"
                        )
                        resultsetCheck = conn.execute(qry)
                        results_as_dict_Check = resultsetCheck.mappings().all()
                        df3 = pd.DataFrame(results_as_dict_Check)
                        qrydf3 = []
                        sumAll = 0
                        for a,b in df3.iterrows():
                            sumAll += int(b['จำนวนชิ้น '])
                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                        sendApi(UID,qrydf3,sumAll)
                    else:
                        pass
                elif i['Product Type'] == 'MINI EXCAVATOR':
                    print('MINI EXCAVATOR')
                    laborvalue = row['LV Main Type']
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
                        sumAll = 0
                        for a,b in df3.iterrows():
                            sumAll += int(b['จำนวนชิ้น'])
                            qrydf3.append(callRow(b['รายการอะไหล่'],b['จำนวนชิ้น']))
                        sendApi(UID,qrydf3,sumAll)
                    else:
                        pass
                elif i['Product Type'] == 'RICE TRANSPLANTER':
                    print('RICE TRANSPLANTER')
                    laborvalue = row['LV Main Type']
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
                        sumAll = 0
                        for a,b in df3.iterrows():
                            sumAll += int(b['จำนวนชิ้น '])
                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น']))
                        sendApi(UID,qrydf3,sumAll)
                    else:
                        pass
                elif i['Product Type'] == 'COMBINE HARVESTER':
                    laborvalue = row['LV Main Type']
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
                        sumAll = 0
                        for a,b in df3.iterrows():
                            sumAll += int(b['จำนวนชิ้น '])
                            qrydf3.append(callRow(b['รายการอะไหล่ที่เปลี่ยน'],b['จำนวนชิ้น ']))
                        sendApi(UID,qrydf3,sumAll)
                    else:
                        pass
            else :
                print('IN KIS')
                queryPeriodical = sa.text("SELECT [description (TH)],[Next Hours],[Next Date] FROM [KIS Data].[dbo].[Engine_Periodical_Check] "
                    "WHERE [VIN] = '" + row['VIN'] + "' AND [Next Date] = '" + datequeryStr + "'"
                    )
                dataPeriodical = conn.execute(queryPeriodical)
                dataPeriodical_as_dick = dataPeriodical.mappings().all()
                sumAll = 0
                if len(dataPeriodical_as_dick) > 0:
                    listCallRow = []
                    for item in dataPeriodical_as_dick:
                        sumAll += 1
                        listCallRow.append(callRow(item['description (TH)'],1))
                    sendApi(UID,listCallRow, sumAll)