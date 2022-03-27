"""
唱歌模块
"""
import config
import requests


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


# [CQ:record,file=http://baidu.com/1.mp3]
def music(gid, word):  # 语音播放音乐模块
    for i in config.music_group_dict.keys():
        if i in word:
            sendGroupMessage(gid, '[CQ:record,file=' + config.music_group_dict.get(i) + ']')

def mu_list(gid,word):
    if ".歌单" in "".join(word):
        sendGroupMessage(gid, "现收录歌曲:"+"、".join(config.music_group_dict.keys())+"\n“注:来首'歌名'即可点歌”")