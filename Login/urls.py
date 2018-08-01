#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-01 11:10:05
# @Last Modified time: 2018-08-01 11:10:21
# @E-mail: 1370465454@qq.com
# @Description: 
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]