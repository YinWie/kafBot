import config
import requests


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


word_list = []
uid_list = []
old_word = ''


def count(word, uid):  # 统计出现次数
    word_list.append(str(word))
    uid_list.append(str(uid))
    # print(word_list, uid_list)
    if len(word_list) > 2:
        if word_list[0] == word_list[1] == word_list[2] and uid_list[0] != uid_list[1] != uid_list[2]:
            del word_list[0]
            del uid_list[0]
            return word
        else:
            del word_list[0]
            del uid_list[0]
            return 0


def reSay(gid, uid, word):  # 是否发过检测
    data = count(word, uid)
    global old_word
    # print(old_word, data)
    if old_word != data and data != 0:
        sendGroupMessage(gid, word.format())
        old_word = data
