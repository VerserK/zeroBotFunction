import requests
import datetime
from pythainlp.util import thai_strftime
import sqlalchemy as sa
import urllib
import pandas as pd

def run():
    true = True
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
        qry = sa.text("SELECT PL.[Name],PL.[TaxId],PL.[UserId],IAC.[VIN],IAC.[Product Type],IAC.[Model], MC.[Name] AS McName FROM [Line Data].[dbo].[Profile Line] PL "
                    "INNER JOIN [CRM Data].[dbo].[ID_Address_Consent] IAC ON PL.[TaxId] = IAC.[Tax ID]"
                    "LEFT JOIN [Line Data].[dbo].[MC Name] MC ON IAC.[VIN] = MC.[VIN]"
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
            
            if i['McName'] == None:
                McName = '-'
            else :
                McName = i['McName']
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
                                        "text": "รถของคุณถึงรอบตรวจเช็กเปลี่ยนถ่ายแล้ว",
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
                                            "text": row['Vehicle Identification Number (Vehicle Identification No.)'],
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
                                            "text": row['Labor Value Main Type'],
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
                                            "text": str(row['Counter for Next Service'])+' ชม.',
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
                                            "text": str(row['Counter for Next Service'])+' ชม.',
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