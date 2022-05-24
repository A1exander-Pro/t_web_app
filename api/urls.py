from django.urls import path, re_path, include

from pages.views import TelegramUserListView
from .views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('users/', UserListView.as_view(), name='api-users'),
    path('telegram-users/', TelegramUsersListView.as_view(), name='api-telegram-users'),

]


urlpatterns = format_suffix_patterns(urlpatterns)