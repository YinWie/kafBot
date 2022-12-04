#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :KaBot 
@File    :Global_config.py
@Author  :音尾様
@Date    :2022/11/7 下午 10:36 
@email   :1327540662@qq.com
@function:全局配置
'''
"""服务ip配置"""
post = 'http://127.0.0.1:5700/'
host = "192.168.0.16"
port = 5000

"""机器人全局参数"""
kaBotUser = ""  # 花宝qq号
kaBotName = "花宝"  # 花宝名
"""群配置项"""
kaf_group_list = ['']  # 监控群号
# 管理员列表
admin = []  


# 定时播报 时间名:[h,m,s]
times = {'hello': [7, 0]}
# 演唱会问答
live_group_dict = {}


def getTime(name):
    return times.get(name)


def getPort():
    return port


def getPost():
    return post


def getHost():
    return host
