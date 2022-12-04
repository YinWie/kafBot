# -*- coding: UTF-8 -*-
'''
@Project :KafBot 
@File    :Song.py
@Author  :音尾様
@Date    :2022/10/23 下午 11:44 
@email   :1327540662@qq.com
@function:花谱歌
'''
from config import Music_config  as Mconfig
from util.CqUtil.CQ_tool import cq_tool


class SongFun():
    Send = cq_tool()

    def play(self, gid, word):
        if Mconfig.keyWord in word:  # 来首音乐
            for i in Mconfig.kaf_music_dict.keys():
                if i in word:
                    self.Send.sendGroupMessage(gid, '[CQ:record,file=' + Mconfig.kaf_music_dict.get(i) + ']')
                    break
        elif Mconfig.keySheet in "".join(word):
            self.Send.sendGroupMessage(gid, "现收录歌曲:" + "、".join(Mconfig.kaf_music_dict.keys()) + "\n“注:来首'歌名'即可点歌”")
