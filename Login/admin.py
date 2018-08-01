#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-01 11:10:05
# @Last Modified time: 2018-08-01 14:35:44
# @E-mail: 1370465454@qq.com
# @Description: 
from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)
