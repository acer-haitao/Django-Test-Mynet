# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 16:14
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : search_indexes.py
# @Software: PyCharm
from haystack import indexes

from .models import job51


class job51Index(indexes.SearchIndex, indexes.Indexable):# Post 创建一个索引
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return job51

    def index_queryset(self, using=None):
        return self.get_model().objects.all()