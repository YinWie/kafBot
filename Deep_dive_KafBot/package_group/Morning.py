#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :KafBot 
@File    :Morning.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:43 
@email   :1327540662@qq.com
@function:早上好
'''
from config import Global_config as config
from util.CqUtil.CQ_tool import cq_tool
import time


class Hello():
    Send = cq_tool()
    cont = True

    def hello_time(self, gid):

        now_time_h = int(time.localtime(time.time()).tm_hour)
        now_time_m = int(time.localtime(time.time()).tm_min)
        if now_time_h == config.getTime("hello")[0] and now_time_m == config.getTime("hello")[1] and self.cont == True:
            img = '[CQ:image,file=guild-images/hello.jpg]'
            self.Send.sendGroupMessage(gid, img.format())  # 发送早安图片
            time.sleep(1)  # 休眠防止文字冲突
            # kafRimSay(gid)  # 伤痛文学
            self.Send.sendGroupMessage(gid, '[CQ:record,file=hello.mp3]')
            time.sleep(1)
            # live_day(gid)  # live提醒
            self.cont = False
            time.sleep(70)
        elif now_time_h == config.getTime("hello")[0] and now_time_m == config.getTime("hello")[1] + 1:
            self.cont  = True
