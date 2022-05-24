from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=20, verbose_name='ФИО', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username