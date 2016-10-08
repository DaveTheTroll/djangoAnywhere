'''
Created on 8 Oct 2016

@author: dave.barnett
'''

from django.conf.urls import url

from . import views

app_name = 'TestWeb'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

