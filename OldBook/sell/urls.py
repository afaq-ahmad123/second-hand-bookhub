from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.sale, name='sale-url'),
    path('add/', views.add, name='add_url'),
]