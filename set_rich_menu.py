'''
參考文件：https://medium.com/enjoy-life-enjoy-coding/使用-python-為-line-bot-建立獨一無二的圖文選單-rich-menus-7a5f7f40bd1
'''

import requests
import json

headers = {"Authorization":"Bearer 42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "點我收合選單",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
          "action": {"type": "message", "text": "行程規劃"}
        },
        {
          "bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
          "action": {"type": "message", "text": "飯店資訊"}
        },
        {
          "bounds": {"x": 1666, "y": 0, "width": 833, "height": 843},
          "action": {"type": "message", "text": "目前天氣"}
        },
        {
          "bounds": {"x": 0, "y": 834, "width": 833, "height": 843},
          "action": {"type": "message", "text": "餐廳資訊"}
        },
        {
          "bounds": {"x": 833, "y": 834, "width": 833, "height": 843},
          "action": {"type": "message", "text": "旅遊指南"}
        },
        {
          "bounds": {"x": 1666, "y": 834, "width": 833, "height": 843},
          "action": {"type": "message", "text": "簡易用語"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)


# ###############
# # 每更新一次menu picture，就必須request取得新的api驗證碼

# # upload pictures

# from linebot import (
#     LineBotApi, WebhookHandler
# )

# line_bot_api = LineBotApi('42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=')

# with open("/Users/peterlin/Documents/Python/LineBOT/jojo/menu_pictures/menu_wallpaper.001.jpeg", 'rb') as f:
#     line_bot_api.set_rich_menu_image(json.loads(req.text)['richMenuId'], "image/jpeg", f)
    
    
# ################
    
# # start rich menu

# import requests

# headers = {"Authorization":"Bearer 42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=","Content-Type":"application/json"}

# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+json.loads(req.text)['richMenuId'],
#                        headers=headers)

# print(req.text)