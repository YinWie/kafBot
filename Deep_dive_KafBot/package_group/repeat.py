# -*- coding: UTF-8 -*-
'''
@Project :KafBot 
@File    :repeat.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:43 
@email   :1327540662@qq.com
@function:复读模块
'''

from util.CqUtil.CQ_tool import cq_tool


class Reread():
    Send = cq_tool()
    word_list = []
    uid_list = []
    old_word = ''  # 记录复读过词汇

    def Trigger(self, gid, uid, word):  # 是否发过检测
        data = self._count(word, uid)
        if self.old_word != data and data != 0 and data != None:
            self.Send.sendGroupMessage(gid, word.format())
            self.old_word = data
        else:
            return 0

    def _count(self, word, uid):  # 统计出现次数
        self.word_list.append(str(word))
        self.uid_list.append(str(uid))
        if len(self.word_list) > 2:
            if self.word_list[0] == self.word_list[1] == self.word_list[2] and self.uid_list[0] != self.uid_list[1] != \
                    self.uid_list[2]:
                del self.word_list[0]
                del self.uid_list[0]
                return word
            else:
                del self.word_list[0]
                del self.uid_list[0]
                return 0
