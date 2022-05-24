from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('telegram', TelegramUserListView.as_view(), name='t_users'),
]