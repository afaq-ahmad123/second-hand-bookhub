from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login-url'),
    path('add/', views.add_user, name='add_user'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register_user'),
    path('del/', views.del_user, name='del_user'),
]