# -*- coding: UTF-8 -*-
'''
@Project :KafBot 
@File    :CQ_tool.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:45 
@email   :1327540662@qq.com
@function:封装cq-http库
'''
from config import Global_config as config
import requests


class cq_tool(object):
    # 发送群消息
    def sendGroupMessage(self, gid, message):
        """
        :param gid: group_id
        :param message:group_say message
        :return:
        """
        url = '{0}send_group_msg?group_id={1}&message={2}'.format(config.getPost(), gid, message)
        requests.get(url=url)
    # 禁言方法
    def sendGroupBan(self, gid, ban_id, ban_time):
        """
        :param gid: group_id
        :param ban_id: user_id
        :param duration_time: ban_time
        :return:
        """
        url = '{0}set_group_ban?group_id={1}&user_id={2}&duration={3}'.format(
            config.getPost(), gid, ban_id, ban_time)
        requests.get(url=url)

