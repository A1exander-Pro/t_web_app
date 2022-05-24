from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, View, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index_2.html'


class TelegramUserListView(LoginRequiredMixin, TemplateView):
    template_name = 'telegram_user_list.html'

   
