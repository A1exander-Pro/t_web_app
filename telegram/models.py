from django.db import models


class TelegramBotUser(models.Model):
    date = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=255, verbose_name='пользователь', blank=True, null=True)
    user_id = models.CharField(max_length=255, verbose_name='user_id', blank=True, null=True)

    def __str__(self):
        return f'{self.username}'