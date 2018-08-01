#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-07-31 16:55:24
# @Last Modified time: 2018-07-31 16:56:17
# @E-mail: 1370465454@qq.com
# @Description: 


from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")