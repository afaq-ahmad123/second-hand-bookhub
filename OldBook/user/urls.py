from django.urls import path
from . import views

urlpatterns = [
    path('', views.prof, name='profile-url'),
    path('edit/', views.edit, name='edit-url'),
]