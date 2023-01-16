## 每更新一次menu picture，就必須request取得新的api驗證碼
# upload pictures

from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=')

with open("./menu_pictures/menu_wallpaper.001.jpeg", 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-a409b50a7122cddede7e664c527e19da', "image/jpeg", f)
    
    
################
    
# start rich menu

import requests

headers = {"Authorization":"Bearer 42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-a409b50a7122cddede7e664c527e19da',
                       headers=headers)

print(req.text)