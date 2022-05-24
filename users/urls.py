from django.urls import path
from .views import *


urlpatterns = [
    path('users', UserListView.as_view(), name='users'),
    path('users/<int:user_id>', UserDetailView.as_view(), name='user'),
    path('create_user', UserCreate.as_view(), name='create_user'),
    path('update_user/<int:user_id>', UserUpdate.as_view(), name='update_user'),
    path('delete_user/<int:user_id>', UserDelete.as_view(), name='delete_user'),

]