#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-01 11:10:05
# @Last Modified time: 2018-08-02 09:29:14
# @E-mail: 1370465454@qq.com
# @Description:
from django.db import models
import datetime
from django.utils import timezone
    
        
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
