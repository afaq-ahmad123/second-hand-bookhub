"""OldBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    #path('adminsite/', adminsite.site.urls),
    #path('', include('home.urls')),
    path('ad/', include('adminsite.urls'), name="adminsite"),
    path('home/', include('home.urls')),
    path('profile/', include('user.urls')),
    path('login/', include('login.urls'), name="login"),
    path('chat/', include('chat.urls')),
    path('404/', include('found.urls')),
    path('', RedirectView.as_view(url='login/')),
    path('sell/', include('sell.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
