from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

import json
import requests
import configparser
from weather_today import getWeather

app = Flask(__name__)

# Channel Access Token, Channel Secret
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# line_bot_api = LineBotApi('42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=')
# handler = WebhookHandler('9e9ada2298a9af1d6c3ae46dd4f1e613')

line_bot_api.push_message('U567164f87f856adc5aa8c413efdc8adf',
    TextSendMessage(text='Meow'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST']) # add "/callback" before Webhook URL in LineDev setting 
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # if event.message.text=='給我檔案':
    #     message = TextSendMessage(text='https://devdocs.line.me/files/sticker_list.pdf')
    #     line_bot_api.reply_message(event.reply_token, message)
   
    # elif event.message.text=='給我圖片':
    #     url = 'https://i.imgur.com/wlvvGb6.jpg'
    #     message = ImageSendMessage(
    #     original_content_url= url,
    #     preview_image_url=url)
    #     line_bot_api.reply_message(event.reply_token, message)
   
    # elif event.message.text=='liff':
    #     message = TextSendMessage(text='line://app/1595926327-1BpoJNgL')
    #     line_bot_api.reply_message(event.reply_token, message)

    # else event.message.text=='pdf':
    #     message = TextSendMessage(text='http://www.africau.edu/images/default/sample.pdf')
    #     line_bot_api.reply_message(event.reply_token, message)
    # else:
    #     message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=isinstance(event.message, ImageMessage))])
    

    # 目前天氣
    if event.message.text=='目前天氣':
        weather = getWeather()
        message = TextSendMessage(
            text='目前峴港氣溫為 ' + str(weather['temp_now']) + '°C\n' +
                '12小時氣溫預報: ' +  str(weather['temp_min']) + ' ~ ' + str(weather['temp_max']) + '°C' +
                '，' + weather['desc'])
        line_bot_api.reply_message(event.reply_token, message)

    # 飯店資訊
    if event.message.text=='飯店資訊':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='飯店資訊',
                text='請點選住宿日期',
                actions=[
                    MessageTemplateAction(
                        label='1/18(三)',
                        text='1/18(三)'
                    ),
                    MessageTemplateAction(
                        label='1/19(五)',
                        text='1/19(五)'
                    ),
                    MessageTemplateAction(
                        label='1/20(六)',
                        text='1/20(六)'
                    ),
                    MessageTemplateAction(
                        label='1/21~22(日一)',
                        text='1/21~22(日一)'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='1/18(三)':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix8.agoda.net/hotelImages/400345/-1/85c1e86f7e351aa1bd4362a7ba9f14ae.jpg?ca=18&ce=1&s=1024x768',
                title='會安海濱水療度假村',
                text='Bel Marina Hoi An Resort',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='會安海濱水療度假村\n'+'127 Nguyễn Phúc Tần, Phường Minh An, Hội An, Quảng Nam \n' + 'https://goo.gl/maps/hmAFuceSC6mRKf727'
                    ),
                    MessageTemplateAction(
                        label='電話',
                        text='+84 236 3966 888'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='1/19(五)':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix8.agoda.net/hotelImages/1985160/-1/b765c9fdc14f30578a7ad8d3db2cae2e.jpg?ca=0&ce=1&s=1024x768', 
                title='Vinpearl度假村Villa',
                text='Vinpearl Resort & Spa Đà Nẵng',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='Vinpearl度假村Villa\n'+'23 Trường Sa, Hoà Hải, Ngũ Hành Sơn, Đà Nẵng, Việt Nam \n' + 'https://goo.gl/maps/WBCF7FzWVmK4XQbz5'
                    ),
                    MessageTemplateAction(
                        label='電話',
                        text='+84 24 3880 3880'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if event.message.text=='1/20(六)':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix8.agoda.net/hotelImages/2613181/-1/d1e55d328306db70d4d728512d3238db.jpg?ca=17&ce=1&s=1024x768',
                title='峴港君主飯店',
                text='Monarque Hotel',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='峴港君主飯店\n'+'238 Võ Nguyên Giáp, Phước Mỹ, Sơn Trà, Đà Nẵng, Việt Nam \n' + 'https://goo.gl/maps/bu1RSYi1kCmcJd9w9'
                    ),
                    MessageTemplateAction(
                        label='電話',
                        text='+84 236 3588 888'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if event.message.text=='1/21~22(日一)':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix8.agoda.net/hotelImages/6250275/-1/2f7569a08235dbfde10938da8d22c137.jpg?ca=7&ce=1&s=1024x768',
                title='亞沃拉精品酒店',
                text='AVORA Boutique Hotel',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='亞沃拉精品酒店\n'+'136 Đ. Lê Duẩn, Thạch Thang, Hải Châu, Đà Nẵng, Việt Nam \n' + 'https://goo.gl/maps/gPRwPMwqpQUcX5cf6'
                    ),
                    MessageTemplateAction(
                        label='電話',
                        text='+84 236 3538 888'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    # if event.message.text=='格蘭德精選水療飯店':
    #     buttons_template = TemplateSendMessage(
    #         alt_text='Buttons Template', 
    #         template=ButtonsTemplate(
    #             thumbnail_image_url = 'https://pix10.agoda.net/hotelImages/10556245/-1/b3e1f06089bee881678667839aeef11a.jpg?s=1024x768',
    #             title='格蘭德精選水療飯店',
    #             text='Grande Collection Hotel & Spa',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='地址',
    #                     text='格蘭德精選水療飯店\n'+'46-48 Bát Sứ, Hàng Bồ, Hoàn Kiếm, Hà Nội, Việt Nam \n'+'https://goo.gl/maps/qdGdqaZTAT1WgRHw5'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='聯絡電話',
    #                     text='+84 91 819 46 48'
    #                 )
    #               ]
    #            )
    #          )
    #     line_bot_api.reply_message(event.reply_token, buttons_template)
    #     last_sentence.update({'userid': user_id, 'val':'Arban'})
    #     return 0

    if event.message.text=='行程資訊':
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix10.agoda.net/hotelImages/8407840/-1/d35ec6f5cf703a04f1dca8473c7b92e9.jpg?s=1024x768',
                title='還劍生態精品飯店',
                text='Eco Boutique Hotel Hoan Kiem',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='還劍生態精品飯店\n'+'5A Cửa Đông, Hàng Bồ, Hoàn Kiếm, Hà Nội, Việt Nam \n'+'https://goo.gl/maps/8qFktAbHUShevXzb7'
                    ),
                    MessageTemplateAction(
                        label='聯絡電話',
                        text='+84 24 3717 3006'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        last_sentence.update({'userid': user_id, 'val':'Arban'})
        return 0

    # 旅程資訊
    if event.message.text=='旅遊指南':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='旅程資訊',
                text='請點選服務',
                actions=[
                    MessageTemplateAction(
                        label='班機時間',
                        text='班機時間'
                    ),
                    MessageTemplateAction(
                        label='購物資訊',
                        text='購物資訊'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    # 班機時間
    if event.message.text=='班機時間':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://img.uupon.tw/upload/store/3335b2eb03000002ebcc.png',
                title='中華航空',
                text='班機資訊',
                actions=[
                    MessageTemplateAction(
                        label='去程：台灣 - 峴港',
                        text='✈️航班 CI787\n 1/18\n 飛行時間：07:15 ~ 09:20\n 航廈：TPE(T1) > DAD(T2)'
                    ),
                    MessageTemplateAction(
                        label='回程：峴港 - 台灣',
                        text='✈️航班 CI790\n 1/23\n 飛行時間：17:35 ~ 21:25\n 航廈：DAD(T2) > TPE(T1)'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    # 美食資訊
    if event.message.text=='會安美食':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='會安地區',
                text='精選餐廳',
                actions=[
                    MessageTemplateAction(label='test', text='success'),
                    MessageTemplateAction(
                        label='QuanCaoLauBaLe 高樓麵',
                        text='Quan Cao Lau Ba Le高樓麵\n 地點: https://goo.gl/maps/ryo4p3S6AiXW5SrE7'
                    )
                    # MessageTemplateAction(
                    #     label='Red Bean Restaurant 越南菜',
                    #     text='Red Bean Restaurant 越南菜\n https://www.tripadvisor.com.tw/Restaurant_Review-g298082-d9750905-Reviews-Red_Bean_Restaurant-Hoi_An_Quang_Nam_Province.html\n 地點: https://goo.gl/maps/d6v1Zh4brb2cLLKG7'
                    # ),     
                    # MessageTemplateAction(
                    #     label="Nhan's kitchen 越南菜",
                    #     text="Nhan's kitchen 越南菜\n https://www.tripadvisor.com.tw/Restaurant_Review-g298082-d12453466-Reviews-Nhan_s_Kitchen-Hoi_An_Quang_Nam_Province.html\n 地點: https://goo.gl/maps/TpMufL1ar2KensWv7"
                    # ),     
                    # MessageTemplateAction(
                    #     label='Reaching Out Tea House 茶館',
                    #     text='Reaching Out Tea House 茶館\n https://www.tripadvisor.com.tw/Restaurant_Review-g298082-d3844277-Reviews-Reaching_Out_Tea_House-Hoi_An_Quang_Nam_Province.html\n 地點: https://goo.gl/maps/HA5ufmG7FrrGBkhM6'
                    # )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='餐廳資訊':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='精選餐廳',
                text='請點選地區',
                actions=[
                    MessageTemplateAction(
                        label='峴港',
                        text='峴港美食'
                    ),
                    MessageTemplateAction(
                        label='會安',
                        text='會安美食'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0




@handler.add(MessageEvent, message=ImageMessage)
def handle_imageMessage(event):
    line_bot_api.reply_message(event.reply_token, [TextSendMessage(text="got pic!")])

@handler.add(MessageEvent, message=FileMessage)
def handle_FileMessage(event):
    line_bot_api.reply_message(event.reply_token, [TextSendMessage(text="got file!")])

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""
channel Secret
9e9ada2298a9af1d6c3ae46dd4f1e613


channel access Token
42oQAgkUxRddwO3bhFSDkFqDNqUTLN/HH+d+BVgfwsI+Dqfc+JpjNgkJ6VyPZl2xhjLZ4o8QkZxw1ckfYF6xTwA4zgFsniAPT3fEH26DgT8Re559X3U4QugahKCl1fsusr8T3zBSz591VLbox0i5OlGUYhWQfeY8sLGRXgo3xvw=

"""