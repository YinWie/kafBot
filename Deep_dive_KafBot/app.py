from flask import Flask, request
import config
import api


app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    data = request.get_json()
    api.timer(data)
    if data.get('message_type') is not None:
        message_type = data.get('message_type')
        # 群聊消息
        if message_type == 'group':
            api.receiveGroupMessage(data)  # 发送群消息
        # 个人消息
        if message_type == 'private':
            api.receivePrivateMessage(data)  # 收取私人消息

    elif data.get('notice_type') is not None:  # 收取通知消息
        api.receiveNoticeMessage(data)
    # else:
    #     print('^^^^^^^^^^^')
    #     print(data)
    #     print('^^^^^^^^^^^')

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True,
            host=config.getHost(),
            port=config.getPort())  # 此处的 host和 port对应上面 yml文件的设置
