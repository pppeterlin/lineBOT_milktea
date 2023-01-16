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
@app.route("/callback", methods=['POST'])
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
            text='目前河內氣溫為 ' + str(weather['temp_now']) + '°C\n' +
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
                        label='1/26 ~ 1/29',
                        text='1/26 ~ 1/29'
                    ),
                    MessageTemplateAction(
                        label='1/29 ~ 1/31',
                        text='1/29 ~ 1/31'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='1/26 ~ 1/29':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='飯店資訊',
                text='請點選身份',
                actions=[
                    MessageTemplateAction(
                        label='月君壧',
                        text='格蘭德精選水療飯店'
                    ),
                    MessageTemplateAction(
                        label='余家',
                        text='還劍生態精品飯店'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='1/29 ~ 1/31':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://www.oakwoodasia.com/upload/property/45/1560928731-oakwood-hanoi-lobby-lounge.jpg',
                title='河內橡木公寓',
                text='Oakwood Residence Hanoi',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='河內橡木公寓\n'+'No. 17, Lane 35, Đặng Thai Mai, Quảng An, Tây Hồ, Hà Nội, Việt Nam \n' + 'https://goo.gl/maps/So8J4G6t72Wwupuf7'
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

    if event.message.text=='格蘭德精選水療飯店':
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://pix10.agoda.net/hotelImages/10556245/-1/b3e1f06089bee881678667839aeef11a.jpg?s=1024x768',
                title='格蘭德精選水療飯店',
                text='Grande Collection Hotel & Spa',
                actions=[
                    MessageTemplateAction(
                        label='地址',
                        text='格蘭德精選水療飯店\n'+'46-48 Bát Sứ, Hàng Bồ, Hoàn Kiếm, Hà Nội, Việt Nam \n'+'https://goo.gl/maps/qdGdqaZTAT1WgRHw5'
                    ),
                    MessageTemplateAction(
                        label='聯絡電話',
                        text='+84 91 819 46 48'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        last_sentence.update({'userid': user_id, 'val':'Arban'})
        return 0

    if event.message.text=='還劍生態精品飯店':
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
    
    if event.message.text=='班機時間':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                title='班機時間',
                text='請點選出發地',
                actions=[
                    MessageTemplateAction(
                        label='台灣',
                        text='台灣出發'
                    ),
                    MessageTemplateAction(
                        label='新加坡（蕙廷）',
                        text='新加坡出發'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text=='台灣出發':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://d3jyiu4jpn0ihr.cloudfront.net/wp-content/uploads/sites/6/20190119120151/thumbnail-facebook.jpg',
                title='越竹航空',
                text='班機資訊',
                actions=[
                    MessageTemplateAction(
                        label='去程：台灣 - 河內',
                        text='✈️航班 QH511\n 1/26\n 飛行時間：20:55 ~ 23:40\n 航廈：TPE(T1) > HAN(T2)'
                    ),
                    MessageTemplateAction(
                        label='回程：河內 - 台灣',
                        text='✈️航班 QH510\n 1/31\n 飛行時間：16:10 ~ 20:40\n 航廈：HAN(T2) > TPE(T1)'
                    )
                  ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if event.message.text=='新加坡出發':   
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template', 
            template=ButtonsTemplate(
                thumbnail_image_url = 'https://www.ourglobetrotters.com/wp-content/uploads/2018/10/FlyScoot-Airline-Review.jpg',
                title='酷航',
                text='班機資訊',
                actions=[
                    MessageTemplateAction(
                        label='去程：新加坡 - 河內',
                        text='✈️航班 VJ916\n 1/27\n 飛行時間：14:55 ~ 17:25\n 航廈：SIN(T4) > HAN(T2)'
                    ),
                    MessageTemplateAction(
                        label='回程：河內 - 新加坡',
                        text='✈️航班 TR301\n 1/31\n 飛行時間：11:10 ~ 15:45\n 航廈：HAN(T2) > SIN(T1)'
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