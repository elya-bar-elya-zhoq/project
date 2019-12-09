"""
Definition of urls for DjangoWebProject1.
"""
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from myApp import forms, views
from django.conf.urls import url, include

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('suggestions/', views.indexS, name='indexS'),
    path('suggestions/new_suggestion/', views.new_suggestion, name='new_suggestion'),
    path('suggestions/<int:suggestion_id>/', views.detail, name='detail'),
    path('suggestions/<int:suggestion_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
]