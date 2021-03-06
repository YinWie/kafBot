"""口球模块"""
import config
import requests
import random
import time
import re

dicts = {}


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


# 禁言函数
def ban(gid, ban_id, duration_time):
    url = '{0}set_group_ban?group_id={1}&user_id={2}&duration={3}'.format(
        config.getPost(), gid, ban_id, duration_time)
    requests.get(url=url)


def num(word):
    t1 = time.time()
    if "口他" in word:
        ban_id = re.compile(r"qq=(.*?)]").findall(word)[0]
        return ban_id


def text(gid, uid, word):
    # ban_id = num(word)
    if "口他" in word:
        ban_id = re.compile(r"qq=(.*?)]").findall(word)[0]
        if ban_id not in config.admin:
            ban(gid, ban_id, 1 * 60)


def kill_me(gid, uid, word):
    word = word.replace("一", '1').replace("二", '2').replace("三", '3').replace("ニ", "2").replace("-", "")
    word = word.replace("四", '4').replace("五", '5').replace("六", '6').replace("七", '7').replace("π", "3")
    word = word.replace("八", '8').replace("九", '9').replace("个", "").replace("十", '10').replace("半", "30")
    word = word.replace("壹", '1').replace("俩", '2').replace("两", '2').replace("叁", '3').replace("千", '000')
    word = word.replace("肆", '4').replace("伍", '5').replace("陆", '6').replace("柒", '7').replace("百", '00')
    word = word.replace("捌", '8').replace("玖", '9').replace("个", "").replace("拾", '10').replace("佰", '00')
    word = word.replace('[CQ:at,qq=3182560165]', '花宝').replace(" ", "")
    if "口我" in word and "月" in word:
        ban_t = int(re.compile(r"口我(.*?)月").findall(word)[0])
        if ban_t == 1:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]满足你的愿望,休息1个月'.format(uid))
        else:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'.format(uid))
    elif "口我" in word and "天" in word:
        ban_t = int(re.compile(r"口我(.*?)天").findall(word)[0])
        if ban_t >= 30:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'.format(uid))
        elif ban_t == 0:
            ban(gid, uid, 1 * 60 * 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]想卡我bug,给我休息一小时反省下'.format(uid, ban_t))

        else:
            ban(gid, uid, ban_t * 60 * 60 * 24)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]满足你的愿望,休息{1}天'.format(uid, ban_t))
    elif "口我" in word and "小时" in word:
        ban_t = int(re.compile(r"口我(.*?)小时").findall(word)[0])
        if ban_t / 24 >= 30:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'.format(uid))
        elif ban_t == 0:
            ban(gid, uid, 1 * 60 * 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]想卡我bug,给我休息1小时反省下'.format(uid, ban_t))
        else:
            ban(gid, uid, ban_t * 60 * 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]满足你的愿望,休息{1}小时'.format(uid, ban_t))
    elif "口我" in word and "分" in word:
        ban_t = int(re.compile(r"口我(.*?)分").findall(word)[0])
        if ban_t / 60 / 24 >= 30:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'.format(uid))
        elif ban_t == 0:
            ban(gid, uid, 3 * 60 * 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]想卡我bug,给我休息3分钟反省下'.format(uid, ban_t))
        else:
            ban(gid, uid, ban_t * 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]满足你的愿望,休息{1}分'.format(uid, ban_t))
    elif "口我" in word and "秒" in word:
        ban_t = int(re.compile(r"口我(.*?)秒").findall(word)[0])
        if ban_t >= 2588400:
            ban(gid, uid, 2588400)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]不支持口一个月以上,先给你加满'.format(uid))
        elif ban_t <= 60:
            ban(gid, uid, 60)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]我觉得太少了,给你凑个整'.format(uid))
        else:
            ban(gid, uid, ban_t)
            time.sleep(0.1)
            sendGroupMessage(gid, '[CQ:at,qq={0}]满足你的愿望'.format(uid))
    elif "口我" in word or "ロ我" in word or "ロ 我" in word or "口 我" in word or "ko我" in word or "Ko我" in word or "kO我" in word or "KO我" in word:
        ban(gid, uid, 3 * 60)
        time.sleep(0.1)
        sendGroupMessage(gid, '[CQ:at,qq={0}]我不认识,先送你三分钟,好好组织语言在来领取口球'.format(uid))
    elif "bot爬" in word or "花宝爬" in word:
        ban(gid, uid, 60 * 60)
        time.sleep(0.1)
        sendGroupMessage(gid, '[CQ:at,qq={0}]你先爬1小时'.format(uid))

# __all__ = ['text', 'kill_me']
