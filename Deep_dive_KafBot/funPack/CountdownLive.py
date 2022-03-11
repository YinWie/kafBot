from datetime import datetime
import config
import requests

# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


def downDays(day):  # 倒数日
    future = datetime.strptime(day, '%Y-%m-%d %H:%M')
    now = datetime.now()
    delta = future - now
    return delta.days


def liveNum(gid, uid, word):  # 演唱会时间
    day = config.live_group_dict[word]
    if downDays(day) > 0:
        sendGroupMessage(gid, '[CQ:at,qq={0}] 花谱妈妈的{1}演唱会还有{2}天就开始了'.format(uid, word, downDays(day)))
    elif downDays(day) == 0:
        sendGroupMessage(gid, '[CQ:at,qq={0}] 花谱妈妈的{1}演唱会当天举行哦'.format(uid, word))
    elif downDays(day) < 0:
        config.live_group_dict.pop(day)


def liveDay(gid, uid, word: str):  # 演唱会倒计时主函数
    word = word.replace("[CQ:at,qq=3182560165] ", "").replace(" ", "")
    if word == '演唱会':
        num = len(config.live_group_dict.keys())
        name = str(list(config.live_group_dict.keys())).replace("[", "").replace("]", "").replace("'", "")
        sendGroupMessage(gid, '[CQ:at,qq={0}] 花谱妈妈的演唱会有{1}个,分别是:{2}'.format(uid, num, name))
    elif word in list(config.live_group_dict.keys()):
        liveNum(gid, uid, word)
