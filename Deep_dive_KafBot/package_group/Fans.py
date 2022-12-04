#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :KaBot 
@File    :Fans.py
@Author  :音尾様
@Date    :2022/11/20 下午 10:01 
@email   :1327540662@qq.com
@function:粉丝数 未实现
'''

# 神椿说&神椿up粉丝数目

name_id = {"花谱": "488970166", "情绪": "488978908",
           "春猿火": "488970166", "幸祜": "701522855",
           "理芽": "489046950", "瓦利斯": "524933572",
           "VWP": "1636327445", "CIEL": "2066920860",
           "ciel": "2066920860", "vwp": "1636327445",
           "存流": "1634470651", "明透": "1634470651",
           }


def str_of_num(num):
    '''
    递归实现，精确为最大单位值 + 小数点后三位
    '''

    def strofsize(num, level):
        if level >= 2:
            return num, level
        elif num >= 10000:
            num /= 10000
            level += 1
            return strofsize(num, level)
        else:
            return num, level

    units = ['', '万', '亿']
    num, level = strofsize(num, 0)
    if level > len(units):
        level -= 1
    return '{}{}'.format(round(num, 3), units[level])


def reptile(id: str):
    hd = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
    }
    url = "https://api.bilibili.com/x/relation/stat?vmid=" + id
    rst = requests.get(url, headers=hd)
    rst.encoding = "utf-8"
    num = re.compile(r'follower":(.*?)}}').findall(rst.text)[0]
    return str_of_num(int(num))
