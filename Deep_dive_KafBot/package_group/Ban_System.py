# -*- coding: UTF-8 -*-
'''
@Project :KafBot
@File    :Ban_System.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:41 
@email   :1327540662@qq.com
@function:禁言
'''
import random

from util.CqUtil.CQ_tool import cq_tool
import re
import time
from config import Ban_Config, Global_config


class Ban():
    """
    投票禁言
    """
    Send = cq_tool()

    # 投票禁言
    def ballot_Ban(self, gid, uid, word):
        """
        :param gid:
        :param uid:
        :param word:
        :return:
        """
        word = self._format_data_Ban(word)
        if "口[CQ:at,qq=" in word and "all" not in word:
            ban_id = re.compile(r"qq=(.*?)]").findall(word)[0]  # 提取ban_id
            times = round(time.time())  # 获取时间戳
            if ban_id == Global_config.kaBotUser:  # 投票机器人反禁言
                self.Send.sendGroupBan(gid, uid, 60 * 60)  # 触发禁言

                self.Send.sendGroupMessage(gid, Ban_Config.KabBan.format(ban_id))  # 触发回复
                time.sleep(0.1)
            elif ban_id not in Ban_Config.ban_dict:  # 第一票
                Ban_Config.ban_dict.setdefault(ban_id, [1, ban_id, times, uid, 0])
                self.Send.sendGroupMessage(gid, Ban_Config.oneBan.format(ban_id))  # 触发回复
                time.sleep(0.1)
            elif Ban_Config.ban_dict[ban_id][3] == uid or Ban_Config.ban_dict[ban_id][4] == uid:  # 重复投票
                self.Send.sendGroupMessage(gid, Ban_Config.reBan.format(ban_id))  # 触发回复
                time.sleep(0.1)
            elif Ban_Config.ban_dict[ban_id][2] + Ban_Config.banTime >= times and Ban_Config.ban_dict[ban_id][
                0] < 2:  # 第二票
                Ban_Config.ban_dict[ban_id][0] += 1
                Ban_Config.ban_dict[ban_id][4] = uid
                self.Send.sendGroupMessage(gid, Ban_Config.twoBan.format(ban_id))  # 触发回复
                time.sleep(0.1)
            else:
                if Ban_Config.ban_dict[ban_id][2] + Ban_Config.banTime >= times:  # 第三票
                    ban_time = random.randint(Ban_Config.ban_Start, Ban_Config.ban_end)  # 定义口球范围 秒()
                    self.Send.sendGroupMessage(gid, Ban_Config.threeBan.format(ban_id, ban_time))  # 触发回复
                    self.Send.sendGroupBan(gid, ban_id, ban_time * 60)  # 触发禁言
                    time.sleep(0.1)
                Ban_Config.ban_dict.pop(ban_id)
        elif Global_config.kaBotName + "爬" in word:
            self.Send.sendGroupMessage(gid, Ban_Config.KabPa.format(uid))  # 触发回复
    # 自我禁言
    def Autisic(self, gid, uid, word):
        """
        :param gid:
        :param uid:
        :param word:
        :return:
        """
        judge = Ban_Config.judge
        word = self._format_data_Aut(word)
        if judge in word and "月" in word:  # 自口月处理
            ban_t = int(re.compile(r"口我(.*?)月").findall(word)[0])
            if ban_t == 1:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_one.format(uid))
            else:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))

        elif judge in word and "天" in word:  # 自口天处理
            ban_t = int(eval(re.compile(r"口我(.*?)天").findall(word)[0]))
            if ban_t >= 30:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))
            elif ban_t == 0:
                self.Send.sendGroupBan(gid, uid, 24 * 60 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.day_bug.format(uid, ban_t))

            else:
                self.Send.sendGroupBan(gid, uid, ban_t * 60 * 60 * 24)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.day.format(uid, ban_t))

        elif judge in word and "小时" in word:  # 自口时处理
            ban_t = int(eval(re.compile(r"口我(.*?)小时").findall(word)[0]))
            if ban_t / 24 >= 30:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))
            elif ban_t == 0:
                self.Send.sendGroupBan(gid, uid, 1 * 60 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.hour_bug.format(uid, ban_t))
            else:
                self.Send.sendGroupBan(gid, uid, ban_t * 60 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.hour.format(uid, ban_t))

        elif judge in word and "时" in word:  # 自口小时处理
            ban_t = int(eval(re.compile(r"口我(.*?)时").findall(word)[0]))
            if ban_t / 24 >= 30:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))
            elif ban_t == 0:
                self.Send.sendGroupBan(gid, uid, 1 * 60 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.hour_bug.format(uid, ban_t))
            else:
                self.Send.sendGroupBan(gid, uid, ban_t * 60 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.hour.format(uid, ban_t))

        elif judge in word and "分" in word:  # 自口分钟判断
            ban_t = int(eval(re.compile(r"口我(.*?)分").findall(word)[0]))
            if ban_t / 60 / 24 >= 30:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))
            elif ban_t == 0:
                self.Send.sendGroupBan(gid, uid, 3 * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.minute_bug.format(uid, ban_t))
            else:
                self.Send.sendGroupBan(gid, uid, ban_t * 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.minute.format(uid, ban_t))

        elif judge in word and "秒" in word:  # 自口秒判断
            ban_t = int(eval(re.compile(r"口我(.*?)秒").findall(word)[0]))
            if ban_t >= 2588400:
                self.Send.sendGroupBan(gid, uid, 2588400)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.month_exceed.format(uid))
            elif ban_t == 60:
                self.Send.sendGroupBan(gid, uid, 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.second.format(uid))

            elif ban_t < 60:
                self.Send.sendGroupBan(gid, uid, 60)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.second_bug.format(uid))
            else:
                self.Send.sendGroupBan(gid, uid, ban_t)
                time.sleep(0.1)
                self.Send.sendGroupMessage(gid, Ban_Config.second_long.format(uid))

        elif judge in word:
            # "ko我" in word or "Ko我" in word or "kO我" in word or "KO我" in word
            self.Send.sendGroupBan(gid, uid, 3 * 60)
            time.sleep(0.1)
            self.Send.sendGroupMessage(gid, Ban_Config.bug.format(uid))

        if "bot爬" in word or Global_config.kaBotName + "爬" in word:
            self.Send.sendGroupBan(gid, uid, 60 * 60)
            time.sleep(0.1)
            self.Send.sendGroupMessage(gid, Ban_Config.KabPa.format(uid))

    # 投票转换  netName:cq_id
    def _format_data_Ban(self, word):
        """
        :param word:
        :return: word
        """
        for i in Ban_Config.name_uid.keys():
            word = word.replace(i, Ban_Config.name_uid[i])
        return word

    # 自口模糊循环替换
    def _format_data_Aut(self, word):
        key = Ban_Config.Autisic_key
        value = Ban_Config.Autisic_values
        if len(key) != len(value):  # 判断转换列表
            print("请修改配置文件")
            return word
        for i in range(len(key)):  # 循环替换
            word = word.replace(key[i], value[i])
        return word
