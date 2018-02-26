# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 17:04
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : urls.py
# @Software: PyCharm
from comment import views as netcomment
from django.conf.urls import url
app_name=['comment']
urlpatterns = [
    url(r'^net163',netcomment.net163(),name='net163'),
]