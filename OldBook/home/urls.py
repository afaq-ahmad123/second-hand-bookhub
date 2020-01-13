from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home-url'),
    path('cart/', views.home, name='cart-url'),
    path('detail/<book>/', views.detail, name='detail'),
    #re_path(r'^detail/(?P<book>\w+)/$', views.detail, name='detail'),
]