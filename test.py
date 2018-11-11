from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#LINE Access Token
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["wvspKc5gcLEIa7A5u7P5pIzOL9bul3KS7LRhHwXFF/xW/xMFfl0SwV9OFsRlhPZwvJVVHE4hfIKdCaXt0yG7i7vpnF6b2W0vsLNOVWOG7T5dkNKuFt23c5KQe45qkB7CvHoxfTgY0+ZSOSq+4g3rRwdB04t89/1O/w1cDnyilFU="]
#LINE Channel Secret
YOUR_CHANNEL_SECRET = os.environ["7fe7567dd5de6e41182f68b81aeeea02"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
