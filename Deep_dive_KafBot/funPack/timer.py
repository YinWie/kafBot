import config
import requests
import time
from datetime import datetime

cont = True


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


# 倒数日
def liveDays(day):
    future = datetime.strptime(day, '%Y-%m-%d %H:%M')
    now = datetime.now()
    delta = future - now
    return delta.days


# live提醒
def live_day(gid):
    num = len(config.live_group_dict.keys())
    day = config.live_group_dict['毕业live']
    name = str(list(config.live_group_dict.keys())).replace("[", "").replace("]", "").replace("'", "")
    sendGroupMessage(gid, '花谱妈妈的演唱会有{0}个,分别是:{1}'.format(num, name))
    if liveDays(day) > 0:
        sendGroupMessage(gid, '花谱妈妈最近的演唱会还有{0}天就开始了'.format(liveDays(day)))
    elif liveDays(day) == 0:
        sendGroupMessage(gid, '花谱妈妈最近的演唱会当天举行哦,记得要去看哦'.format())


# 早上好主模块

def hello_time(gid):
    global cont
    now_time_h = int(time.localtime(time.time()).tm_hour)
    now_time_m = int(time.localtime(time.time()).tm_min)

    if now_time_h == config.getTime("hello")[0] and now_time_m == config.getTime("hello")[1] and cont == True:
        sendGroupMessage(gid, '[CQ:image,file=guild-images/hello.jpg]'.format())  # 发送早安图片
        time.sleep(1)  # 休眠防止文字冲突
        sendGroupMessage(gid, '[CQ:record,file=hello.mp3]')
        time.sleep(1)
        live_day(gid)  # live提醒

        cont = False
    elif now_time_h == config.getTime("hello")[0] and now_time_m == config.getTime("hello")[1] + 1:
        cont = True

    # print(now_time_h, now_time_m, now_time_s) #测试log
