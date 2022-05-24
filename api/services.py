from users.models import *
from telegram.models import *


def get_users():
    users = UserProfile.objects.all().values('id', 'username', 'full_name', 'date_joined')
    users_list = [{'id': obj['id'],
                   'username': obj['username'],
                   'full_name': obj['full_name'],
                   'date_joined': obj['date_joined'], } for obj in users]
    return users_list


def get_telegram_users():
    users = TelegramBotUser.objects.all().values('id', 'username', 'user_id', 'date')
    users_list = [{'id': obj['id'],
                   'username': obj['username'],
                   'user_id': obj['full_name'],
                   'date': obj['date'], } for obj in users]
    return users_list