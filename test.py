import os
import sys
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

app = Flask(__name__)

# 環境変数からchannel_secret・channel_access_tokenを取得
channel_secret = os.environ['7fe7567dd5de6e41182f68b81aeeea02']
channel_access_token = os.environ['VvZgXvOXplbiNNWVYX7I3P7XM81vOiMM25D8GqewH2CaKVhqrIgM0fytVVK+FYJWvJVVHE4hfIKdCaXt0yG7i7vpnF6b2W0vsLNOVWOG7T46zbqxMmbT5NWRHb/BzlGwR1tpz9h9kys/HXYgiVuasgdB04t89/1O/w1cDnyilFU=']

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/")
def hello_world():
    return "hello world!"
