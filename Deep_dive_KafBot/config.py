import funPack.CountdownLive

# post = 'http://192.168.0.105:5700/'
# host = "192.168.0.105"
post = 'http://127.0.0.1:5700/'
host = "127.0.0.1"
port = 5000
kaf_group_list = [
    '769411708'
]


live_group_dict = {'毕业live': '2022-03-26 19:59',
                   '魔女集会': '2022-04-15 19:59',
                   '现象': '2022-04-16 19:59'}



def getPort():
    return port


def getPost():
    return post


def getHost():
    return host
