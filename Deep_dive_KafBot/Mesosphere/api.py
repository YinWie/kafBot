#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :KaBot 
@File    :api.py
@Author  :音尾様
@Date    :2022/11/2 下午 9:48 
@email   :1327540662@qq.com
@function:
'''
from config import Global_config, Ban_Config
from util import apiUtil as fun


# 是否监视该群
def isWatchGroup(gid):
    return str(gid) in Global_config.kaf_group_list


# 是否呼叫bot
def callKafBot(word):
    return '[CQ:at,qq=3182560165]' in word


# 收取群消息

def receiveGroupMessage(data):
    gid = data.get('group_id')  # User_id
    uid = data.get('sender').get('user_id')  # Global_id
    word = data.get("raw_message")  # message
    if isWatchGroup(gid):  # 是否监管群
        if callKafBot(word):  # at Kabot 功能
            pass
        fun.ban.ballot_Ban(gid, uid, word)  # 投票禁言
        fun.ban.Autisic(gid, uid, word)  # 自口
        fun.song.play(gid, word)  # 唱歌
        if Ban_Config.ban_judge not in word:
            fun.resay.Trigger(gid, uid, word)  # 复读
        # kafRimSay(gid, word)  # 青春小作文
        if str(gid) in '799086549':  # 测试群
            pass
        print(gid, uid, word)  # 打印log


def GlobalMessage(data):
    fun.morning.hello_time('769411708')  # 早上好


# 收取私人消息
def receivePrivateMessage(data):
    print(data)
    # sendPrivateMessage(data.get('sender').get('user_id'), data.get('message'))


# 收取通知消息
def receiveNoticeMessage(data):
    print(data)
    pass
