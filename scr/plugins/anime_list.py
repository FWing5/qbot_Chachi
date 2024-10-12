import requests
import json
import time


def get_anime_list():

    url = "https://api.bgm.tv/calendar"
    
    response = requests.get(url)

    data = response.json()
    with open('testdata.json', 'w') as file:
        json.dump(data,file)

get_anime_list()

# def format_weather(city_name):

#     city_encoded = city_name  # 重庆的URL编码
#     weather_data = get_weather(city_encoded)

#     # 检查是否返回了错误
#     if 'error' in weather_data:
#         return weather_data['error']
#     else:
#         # 实时天气
#         realtime_weather = weather_data['realtime']
#         result = f"实时天气:" + "\n" +  f"{realtime_weather['info']}, 温度: {realtime_weather['temperature']}℃, 湿度: {realtime_weather['humidity']}%, 风向: {realtime_weather['direct']}, 风力: {realtime_weather['power']}级, AQI: {realtime_weather['aqi']}"
#         # 未来几天的天气
#         result = result + "\n" + "未来几天的天气:"
#         for day in weather_data['future']:
#             result = result + "\n" + f"日期: {day['date']}, 天气: {day['weather']}, 温度: {day['temperature']}, 风向: {day['direct']}"
#         return result
