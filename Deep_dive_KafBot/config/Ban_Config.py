#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :KaBot 
@File    :Ban_Config.py
@Author  :音尾様
@Date    :2022/11/7 下午 10:35 
@email   :1327540662@qq.com
@function:禁言配置
'''
import random

"""固定参数"""
ban_dict = {}  # {qq:[num,time.hour,[xxx，xxx,xxx]]} 投票参数
"""可变参数"""
banTime = 1800  # 定义口球释放时间/S
ban_Start = 15
ban_end = 35
ban_judge="口"

"""网名qq号转换"""
name_uid = {"小旦": "[CQ:at,qq=875314086]", "太二": "[CQ:at,qq=1349556226]",
            "猫又": "[CQ:at,qq=1394354856]", "花弑": "[CQ:at,qq=1678838712]",
            "TE": "[CQ:at,qq=1154117230]", "te": "[CQ:at,qq=1154117230]",
            "花宝": "[CQ:at,qq=3182560165]", "咕子": "[CQ:at,qq=3232440139]"}

"""回复语句定义 注:{0}接收ban的qq_id ,{1}接收口球时间"""
KabBan = "居然敢口我,[CQ:at,qq={0}]我直接送你1小时,[CQ:face,id=277]"  # 口花宝禁言
reBan = "花宝提醒:[CQ:at,qq={0}]已经口过这个人了,换个人口吧[CQ:face,id=277]"  # 重复禁言
oneBan = "花宝提醒:[CQ:at,qq={0}]你被口啦,一小时内集齐3次有小惊喜[CQ:face,id=277]"  # 第一次投票
twoBan = "花宝提醒:[CQ:at,qq={0}]你被口两次啦,在来一次小礼物就来咯[CQ:face,id=277]"  # 第二次投票
threeBan = "花宝提醒:恭喜[CQ:at,qq={0}]获得{1}分钟口球,开不开心,感觉不够等禁言结束自己加[CQ:face,id=277]"  # 禁言生效
KabPa = "[CQ:at,qq={0}]你先爬1小时"  # 花宝爬

"""自口禁言处理对照表 key 对应values"""
Autisic_key = ["一", "二", "三", "四", "五", "六", "七", "八", "九",
               "壹", "俩", "两", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾",
               "ニ", "-", "π", ".", "百", "千", "佰", "个", '[CQ:at,qq=3182560165]',
               " ", "□", "ロ", ]
Autisic_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "1", "2", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                  "2", "", "3", "", "00", "000", "00", "", "",
                  " ", "口", "口"
                  ]
"""触发关键字"""
judge = "口我"

"""自口配置文件"""
month_exceed = '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'
month_one = '[CQ:at,qq={0}]满足你的愿望,休息1个月'
day_bug = '[CQ:at,qq={0}]想卡我bug,给我休息一天反省下'
day = '[CQ:at,qq={0}]满足你的愿望,休息{1}天'
hour_bug = '[CQ:at,qq={0}]想卡我bug,给我休息1小时反省下'
hour = '[CQ:at,qq={0}]满足你的愿望,休息{1}小时'
minute_bug = '[CQ:at,qq={0}]想卡我bug,给我休息3分钟反省下'
minute = '[CQ:at,qq={0}]满足你的愿望,休息{1}分'
second = '[CQ:at,qq={0}]满足你的愿望,休息60秒'
second_bug = '[CQ:at,qq={0}]我觉得太少了,给你凑个整'
second_long = '[CQ:at,qq={0}]满足你的愿望'
bug = '[CQ:at,qq={0}]我不认识,先送你三分钟,好好组织语言在来领取口球'
