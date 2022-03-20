import requests
import config
from funPack.CountdownLive import liveDay
from funPack.repeat import reSay
from funPack.timer import hello_time
from funPack.song import music, mu_list


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


# 是否监视该群
def isWatchGroup(gid):
    return str(gid) in config.kaf_group_list


# 是否呼叫bot
def callKafBot(word):
    return '[CQ:at,qq=3182560165]' in word


# 收取群消息
def receiveGroupMessage(data):
    gid = data.get('group_id')
    uid = data.get('sender').get('user_id')
    word = data.get("raw_message")
    if isWatchGroup(gid) and callKafBot(word):  # 艾特功能
        liveDay(gid, uid, word)  # 倒计时功能
    if isWatchGroup(gid):
        mu_list(gid, word)  # 歌单
        reSay(gid, uid, word)  # 复读姬功能
        if "来首" in word:  # 来首音乐
            music(gid, word)
    if str(gid) in '799086549':
        liveDay(gid, uid, word)
        music(gid, word)
        # reSay(gid, uid, word)

    print(gid, uid, word)

    # print('\n\n\n', data)


#  定时播报
def timer(data):
    hello_time('769411708')  # 早上好特定群发送图片和内容


# 收取私人消息
def receivePrivateMessage(data):
    print(data)
    # sendPrivateMessage(data.get('sender').get('user_id'), data.get('message'))


# 收取通知消息
def receiveNoticeMessage(data):
    print(data)
    pass
