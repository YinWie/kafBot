import requests
import config
from funPack.CountdownLive import liveDay
from funPack.repeat import reSay


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
        reSay(gid, uid, word)  # 复读姬功能
    if str(gid) in '799086549':
        liveDay(gid, uid, word)
        # reSay(gid, uid, word)

    print(gid, uid, word)

    # print('\n\n\n', data)


# 收取私人消息
def receivePrivateMessage(data):
    print(data)
    # sendPrivateMessage(data.get('sender').get('user_id'), data.get('message'))


# 收取通知消息
def receiveNoticeMessage(data):
    print(data)
    pass