"""yetiMP3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('ajax/download_yt/', views.download_from_yt, name='download_yt'),
    path('ajax/async/download_yt/', views.download_from_yt_async, name='async/download_yt'),
    path('ajax/async/check_task/', views.check_task, name='async/check_task'),
    path('ajax/download/<str:id>/<str:name>', views.download_mp3, name='download_mp3'),
    path('home/', views.redirect_index, name='home')
]
