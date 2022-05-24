from django.urls import path, include, re_path
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt
from .t_bot import UpdateBot
from .views import WebAppView


urlpatterns = [
    path('webhook/telegram/bot/', csrf_exempt(UpdateBot.as_view()), name='update'),
    path('webapp/', WebAppView.as_view(), name='app'),
]