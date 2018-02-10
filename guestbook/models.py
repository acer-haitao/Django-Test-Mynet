# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 10:14
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : 1.py
# @Software: PyCharm
from django.db import models

# Create your models here.
class Msg(models.Model):
    '''
    姓名，时间，内容，标题
    '''
    username = models.CharField(max_length=256)
    time = models.DateTimeField()
    txt = models.TextField()
    title = models.CharField(max_length=512)

    def __str__(self):
        tpl = '<Msg:[username={username},time={time},txt={txt},title={title}]>'
        return tpl.format(username = self.username, time = self.time, txt = self.txt, title = self.title)
