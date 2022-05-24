from django.http import JsonResponse
from django.views import View
import telebot
from telebot import types
from .models import TelegramBotUser
from django.conf import settings
from .send_message import send_message

token = settings.TOKEN

bot = telebot.TeleBot(token)

update_id = None


class UpdateBot(View):
    def post(self, request, *args, **kwargs):
        global update_id
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        if update_id != update.update_id:
            bot.process_new_updates([update])
            update_id = update.update_id
        return JsonResponse({"ok": True})


@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.from_user.username
    user_id = message.from_user.id
    try:
        t_user = TelegramBotUser.objects.get(user_id=user_id)
    except:
        t_user = TelegramBotUser.objects.create(user_id=user_id, username=username)

    msg = f'Привет, {t_user.username}'
    bot.send_message(message.chat.id, f'{msg}')


@bot.message_handler(content_types="web_app_data")  # получаем отправленные данные
def answer(webAppMes):
    send_message(webAppMes)
    send_message(webAppMes.web_app_data.data)
    bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
