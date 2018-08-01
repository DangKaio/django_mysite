#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-01 11:10:05
# @Last Modified time: 2018-08-01 16:32:31
# @E-mail: 1370465454@qq.com
# @Description: 
from django.urls import path

from . import views
app_name='polls'#命名空间
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('specifics/<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
#改良urlconf
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]