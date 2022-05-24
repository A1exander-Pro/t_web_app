import requests
from django.conf import settings

TOKEN = settings.TOKEN
CHAT_ID = settings.CHAT_ID


def send_message(text: str):
    token = TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = CHAT_ID
    url += token
    method = url + "/sendMessage"
    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })
    if r.status_code != 200:
        raise Exception("post_text error")