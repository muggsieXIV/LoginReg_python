from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_create', views.process_create),
    path('process_login', views.process_login),
    path('welcome', views.welcome),
    path('logout', views.logout),
]
