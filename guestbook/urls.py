# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 10:35
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url,include

from guestbook import views as guest_views

app_name=['guestbook']
urlpatterns = [
    url(r'^deleteid',guest_views.deleteid,name='deleteid'),
    url(r'^delete',guest_views.delete(),name='delete'),
    url(r'^save',guest_views.save,name='save'),
    url(r'^comment',guest_views.comment,name='comment'),
    url(r'^create',guest_views.create,name='create')
]