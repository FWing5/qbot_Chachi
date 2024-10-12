#Chachi主程序
#目前功能：
#       1 收到@时回复（测试功能）
#       2 回复今日/明日新番列表（插件进行中）

import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

from plugins import anime_list

TODAY = 1   #使用常量1代表今天
TMR = 2     #使用常量2代表明天

#读取bot配置文件
test_config = read(os.path.join(os.path.dirname(__file__),"config.yaml"))

#日志记录器
_log = logging.get_logger()


class MyClient(botpy.Client):

    #当bot准备就绪时记录日志
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    #当群聊中bot被@时，调用此方法以表示机器人收到该消息（测试用功能）
    async def on_group_at_message_create(self, message: GroupMessage):
        messageResult = await message._api.post_group_message(
            group_openid=message.group_openid,
              msg_type=0, 
              msg_id=message.id,
              content= f"「{self.robot.name}[4]」收到你@的消息了哦: 「{message.content}」")
        _log.info(messageResult)

        #使用“/每日放送”指令使bot回复今日新番列表
        if "/每日放送" in message.content:
            reply = anime_list.get_anime_list(TODAY)
            
            await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{reply}")
            
        #使用“/明日预告”指令使bot回复明日新番列表
        if "/明日预告" in message.content:
            reply = anime_list.get_anime_list(TMR)
            
            await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0,
                msg_id=message.id,
                content=f"{reply}")
 

if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])