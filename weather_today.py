import requests
import json
import requests
import configparser

def getWeather():
    weather = {'temp_now': None, 'temp_min': None, 'temp_max': None, 'desc': None}
    # 

    try:
        url = "https://api.openweathermap.org/data/2.5/weather?id=1581129&APPID=d36bf1f48799c28847d4b94033fb617d"
        response = requests.get(url)
        dt = response.json()
        weather['temp_now'] = round(dt['main']['temp']-273.15, 1)
    except:
        weather['temp_now'] = 0
    
    try:
        url = "https://api.openweathermap.org/data/2.5/forecast?id=1581129&APPID=d36bf1f48799c28847d4b94033fb617d"
        response = requests.get(url)
        dt = response.json()
        
        tmp_forecast = []
        desc = []
        for i in range(5):
            peroid = dt['list'][i]
            desc.append(peroid['weather'][0]['main'])
            tmp_forecast.append(peroid['main']['temp_min']-273.15)
            tmp_forecast.append(peroid['main']['temp_max']-273.15)
        
        weather['temp_min'] = round(min(tmp_forecast), 1)
        weather['temp_max'] = round(max(tmp_forecast), 1)
        weather['desc'] = max(set(desc), key=desc.count)
    except:
        weather['temp_min'] = weather['temp_max'] = weather['desc'] = 0
    
    translate = {'Clouds':'多雲', 'Clear': '晴朗', 'Rain':'下雨'}
    weather['desc'] = translate[weather['desc']]

    return weather

    
# weather = getWeather()
# print('目前河內氣溫為 ' + str(weather['temp_now']) + '°C\n' +
#                 '12小時氣溫預報: ' +  str(weather['temp_min']) + ' ~ ' + str(weather['temp_max']) + '°C' +
#                 '，' + weather['desc'])
