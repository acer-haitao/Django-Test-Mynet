# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 10:17
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from job51 import views as job_views

urlpatterns = [
    url(r'^job',job_views.job(),name='job51'),
]