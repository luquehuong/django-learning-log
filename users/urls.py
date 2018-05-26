"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
  # Login Page
  url(r'^login/$', login, { 'template_name': 'users/login.html' }, name='login'),
  # Logout Page
  url(r'^logout/$', views.logout_view, name='logout'),
  # Registration Page
  url(r'^register/$', views.register, name='register'),
]