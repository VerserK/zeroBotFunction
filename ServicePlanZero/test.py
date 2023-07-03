data={
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
                "text": str(row['Counter for Next Service']),
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
                "text": str(row['Counter for Next Service']),
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