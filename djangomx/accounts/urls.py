# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^@(?P<username>[\w-]+)$', views.ProfileView.as_view(), name='profile'),

]
