import funPack.CountdownLive

# post = 'http://192.168.0.105:5700/'
# host = "192.168.0.105"
post = 'http://127.0.0.1:5700/'
host = "127.0.0.1"
port = 5000
# 监控群号
kaf_group_list = [
    ''
]
# 管理员列表
admin = []

# 定时播报 时间名:[h,m,s]
times = {'hello': [7, 0]}
# 演唱会问答
live_group_dict = {'魔女集会': '2022-04-15 19:59',
                   '现象': '2022-04-16 19:59',
                   '不可解（叁）狂': '2022-08-24 19:59', }
music_group_dict = {
    "言灵": "/vwp/言灵.mp3",
    "共鸣": "/vwp/共鸣.mp3",

    "糸": "/观测/糸.mp3",
    "忘れてしまえ": "/观测/忘れてしまえ.mp3",
    "心臓と絡繰": "/观测/心臓と絡繰.mp3",
    "quiz": "/观测/quiz.mp3",
    "Re：HEROINES": "/观测/Re：HEROINES.mp3",
    "夜行バスにて": "/观测/夜行バスにて.mp3",
    "未确认少女进行形": "/观测/未确认少女进行形.mp3",
    "エリカ": "/观测/エリカ.mp3",
    "雏鸟": "/观测/雏鸟.mp3",
    "夜が降り止む前に": "/观测/夜が降り止む前に.mp3",
    "不可解": "/观测/不可解.mp3",
    "然后成为花": "/观测/然后成为花.mp3",

    "危ノーマル": "/魔法/危ノーマル.mp3",
    "答案": "/魔法/答案.mp3",
    "私伦理": "/魔法/私伦理.mp3",
    "困惑的心灵感应": "/魔法/困惑的心灵感应.mp3",
    "彷徨": "/魔法/彷徨.mp3",
    "毕生": "/魔法/毕生.mp3",
    "花女": "/魔法/花女.mp3",
    "meru的黄昏": "/魔法/meru的黄昏.mp3",
    "痛みを": "/魔法/痛みを.mp3",
    "景色": "/魔法/景色.mp3",
    "帰り路": "/魔法/帰り路.mp3",
    "魔法feat理芽": "/魔法/魔法feat理芽.mp3",

    "镜子啊镜子": "/组曲/镜子啊镜子.mp3",
    "假想朋友": "/组曲/假想朋友.mp3",
    "あさひAsahi": "/组曲/あさひAsahi.mp3",
    "飛翔するmeme": "/组曲/飛翔するmeme.mp3",
    "拔刀": "/组曲/拔刀.mp3",
    "线香": "/组曲/线香.mp3",
    "春阳": "/组曲/春阳.mp3",

    "那称之为世界": "/其他/那称之为世界.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",
    # "危ノーマル": "/观测/危ノーマル.mp3",

}


def getTime(name):
    return times.get(name)


def getPort():
    return port


def getPost():
    return post


def getHost():
    return host
