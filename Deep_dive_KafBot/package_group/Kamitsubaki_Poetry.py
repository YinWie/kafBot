#-*- coding: UTF-8 -*-
'''
@Project :KafBot 
@File    :Kamitsubaki_Poetry.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:44 
@email   :1327540662@qq.com
@function:神椿文学 未实现
'''
import re

import config
import requests
import random


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


def kafRimSay(gid, word):
    for i in name_id.keys():
        if i in word and "粉丝" in word:
            sendGroupMessage(gid, "哇！b站居然有:" + reptile(name_id[i]) + "人关注{0}".format(i))

    if "花谱诗" in word:  # or "花谱" in word
        with open('./data/kafSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:花谱")
    elif "理芽文学" in word or '理芽' in word and "粉丝" not in word:
        with open('./data/RimSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:理芽")
    elif "春酱碎碎念" in word or '春猿火' in word and "粉丝" not in word:
        with open('./data/harusaruhiSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:春猿火")
    elif "伤痛文学" in word:
        with open('./data/RimSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:理芽")
        with open('./data/kafSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:花谱")
