data = {
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
                "text": "ไอ้แดง 1"
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


address={
    "type": "box",
    "layout": "baseline",
    "contents": [
        {
            "type": "text",
            "text": "จุดที่ (1) :",
            "wrap": true,
            "color": "#818181"
        },
        {
            "type": "text",
            "text": 'ต.'+ str(row['SubDistrict']) + ' อ.' + str(row['District']) + ' จ.' + str(row['Province']) + ' ' + str(row['Country']) + ' (' + str(row['Hour']) +' ชม.)',
            "wrap": true
        }
    ]
}