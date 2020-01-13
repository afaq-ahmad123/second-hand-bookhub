from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.chat, name='chat-url'),
]