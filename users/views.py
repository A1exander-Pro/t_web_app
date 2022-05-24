from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    
    template_name = 'user_list.html'
    model = UserProfile
    context_object_name = 'users'


class UserCreate(LoginRequiredMixin, CreateView):
    model = UserProfile
    template_name = 'forms/add_user_form.html'
    form_class = UserProfileForm
    success_url = 'users'
    
    def get_success_url(self):
        self.object.is_active = True
        self.object.save()
        return reverse('users')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'user.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'


class UserUpdate(LoginRequiredMixin, UpdateView):
    access_object = 'Пользователь - Редактрование'
    model = UserProfile
    template_name = 'forms/update_user_form.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    form_class = UserProfileUpdateForm
    success_url= reverse_lazy('users')
    initial = {'key': 'value'}
    # fields = ['username', 'last_name', 'first_name', 'middle_name', 'hire_date', 'quit_date',  'contract',
    #           'email', 'telephone', 'role', 'is_staff', 'is_active', 'permission', 'to_who_payed']

    # def get_success_url(self):
    #     return reverse('user', kwargs={'user_id': self.object.id})


class UserDelete(LoginRequiredMixin, DeleteView):
    access_object = 'Пользователь - Удаление'
    model = UserProfile
    success_url = reverse_lazy('users')
    template_name = 'forms/user_form_delete.html'
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'