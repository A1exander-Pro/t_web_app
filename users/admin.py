from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "full_name")


admin.site.register(UserProfile, UserProfileAdmin)

