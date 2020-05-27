
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'useradministration'
urlpatterns = [
   path('', views.IndexView.as_view(), name = 'index'),
   path('', views.ProfileView.as_view(), name='profile'),
]