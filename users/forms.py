from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            "placeholder": "username",
        }
    ), label='Username')
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Проверка пароля",
                "class": "form-control"
            }
        ))
    
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            "placeholder": "ФИО",
        }
    ), label='Username')


    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2',
                  'full_name']


class UserProfileUpdateForm(ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password",
    #             "class": "form-control"
    #         }
    #     ))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password check",
    #             "class": "form-control"
    #         }
    #     ))
    
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            "placeholder": "ФИО",
        }
    ), label='Username')
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            "placeholder": "username",
        }
    ), label='Username')


    class Meta:
        model = UserProfile
        fields = ['username', 'full_name', 'email']