from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageMessage,ImageSendMessage
)
import os
import pya3rt

app = Flask(__name__)

# 環境変数
linebot_api = LineBotApi('00rndh6ND1MSPXKA4yHtOilgY+9zKkDxRk0ICZelnDz2wuEhbVtnTg+U8V9XHIbN8lMNSG1DhGSThv/vIMh66vyAibaE3hfnC2WAZfL+lZphQlcYHM8qCa9pewHzhS1yWhyQWQw+fZCSufYuEWk6kAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bb19322823539a5f01a8eca92c13949e')


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
    #ai_message = talk_ai(event.message.text)
    linebot_api.reply_message(
        event.reply_token,
        ImageSendMessage(original_content_url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fdol.ismcdn.jp%2Fmwimgs%2Fa%2Ff%2F-%2Fimg_afa0fad37e6c4d5ce34c01faf54f9e79108563.jpg&imgrefurl=https%3A%2F%2Fdiamond.jp%2Farticles%2F-%2F156184&tbnid=5eUbF4tC8geGtM&vet=12ahUKEwitp_ORwZ_tAhVE6ZQKHYIsAqkQMygAegUIARDWAQ..i&docid=56ZkDmQ8GXH_5M&w=1200&h=630&q=%E7%8A%AC&ved=2ahUKEwitp_ORwZ_tAhVE6ZQKHYIsAqkQMygAegUIARDWAQ',
                         preview_image_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fdol.ismcdn.jp%2Fmwimgs%2Fa%2Ff%2F-%2Fimg_afa0fad37e6c4d5ce34c01faf54f9e79108563.jpg&imgrefurl=https%3A%2F%2Fdiamond.jp%2Farticles%2F-%2F156184&tbnid=5eUbF4tC8geGtM&vet=12ahUKEwitp_ORwZ_tAhVE6ZQKHYIsAqkQMygAegUIARDWAQ..i&docid=56ZkDmQ8GXH_5M&w=1200&h=630&q=%E7%8A%AC&ved=2ahUKEwitp_ORwZ_tAhVE6ZQKHYIsAqkQMygAegUIARDWAQ"))

"""
def talk_ai(word):
    apikey = "DZZcVWVGK24c5c1lm3mup4Mqi3GtlWSC"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(word)
    return reply_message['results'][0]['reply']
"""

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
