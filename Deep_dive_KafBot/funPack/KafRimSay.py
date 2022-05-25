import config
import requests
import random


# 发送群消息
def sendGroupMessage(gid, message):
    url = '{0}send_group_msg?group_id={1}&message={2}'.format(
        config.getPost(), gid, message)
    requests.get(url=url)


def kafRimSay(gid, word):
    if "花谱诗" in word:  # or "花谱" in word
        with open('./data/kafSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:花谱")
    elif "理芽文学" in word or '理芽' in word:
        with open('./data/RimSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:理芽")
    elif "春酱碎碎念" in word or '春猿火' in word:
        with open('./data/harusaruhiSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:春猿火")
    elif "伤痛文学" in word:
        with open('./data/RimSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:理芽")
        with open('./data/kafSayCN.txt', 'r') as f:
            data = f.readlines()
            num = random.randint(0, len(data) - 1)
            sendGroupMessage(gid, data[num] + "by:花谱")
