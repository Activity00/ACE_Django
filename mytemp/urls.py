#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月8日

@author: 武明辉
'''
from django.conf.urls import url

from mytemp import views

app_name='mytemp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^$',views.index2,name='index'),
    ]

