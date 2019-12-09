
"""
Definition of urls for DjangoWebProject1.
"""
from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from myApp import forms, views
from django.conf.urls import url, include

app_name = 'myApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('/news', views.news, name='news'),
]