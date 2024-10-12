import requests
import json
import time

#将会在main中直接被调用的get方法
def get_anime_list(weekday):
    """ 
    获取今日新番目录，返回可直接输出的字符串

    Args:
        weekday(int): 今日为周几，1为周一，7为周日

    Returns:
        (str):当日的新番列表，或是错误信息
    """

    url = "https://api.bgm.tv/calendar"         #bangumiAPI中canlendar的url
    headers = {'accept':'application/json'}     #请求头
    
    response = requests.get(url, headers = headers)     #获取请求内容

    #状态码为200时，请求成功
    if response.status_code == 200:

        #将请求内容转换为json格式
        jsonlist = response.json()

        #整理为输出格式
        for day_data in jsonlist:
            if day_data['weekday']['id'] == weekday:
                weekday_cn = day_data['weekday']['cn']
                weekday_ja = day_data['weekday']['ja']
                items = day_data['items']

                output = f"今天是{weekday_cn}（{weekday_ja}），一共有{len(items)}部新番正在播出：\n"
                for item in items:
                    output += f"{item['name_cn']}（{item['name_ja']}）  评分★{item['rating']['score']}\n"
                output += "该看那部呢？"

        return "茶知好像在火星追番，什么都没有哦"
        
        #生成json文件的测试代码
        # with open('testdata.json', 'w', encoding = 'utf-8') as file:
        #     json.dump(data, file, ensure_ascii=False, indent=4)

    #直接在机器人的回复中报告错误
    else:
        return "告诉飞飞这个对接暗号："+response.status_code

#get_anime_list()