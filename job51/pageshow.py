# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 15:20
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : pageshow.py
# @Software: PyCharm
#自定义分页类
from django.db.models import Q

class Pagination(object):
    """用于Model字段值的选择"""
    def __init__(self):
        pass
    @classmethod
    def create_pagination(self, from_name='', model_name='',
                          cur_page=1, start_page_omit_symbol = '...',
                          end_page_omit_symbol = '...', one_page_data_size=10,
                          show_page_item_len=9,form_post = 'python'):

        # 如果没有输入导入模块需要的相关信息直接退出
        if not from_name or not model_name:
            return None

        import_str = 'from {from_name} import {model_name}'.format(
                from_name = from_name,
                model_name = model_name)
        # 导入模块
        exec(import_str)

        start_pos = (cur_page - 1) * one_page_data_size#开始位置
        end_pos = start_pos + one_page_data_size

        # 查找需要的model数据
        if  form_post:
            find_objs_str = ('{model_name}.objects.filter(Q(jobname__contains="{form_post3}")|Q(date__contains="{form_post2}")|Q(address__contains="{form_post}")|Q(jobname__contains="{form_post1}"))'
                             '[{start_pos}:{end_pos}]'.format(
                    model_name = model_name,
                    start_pos = start_pos,
                    end_pos = end_pos,
                    form_post = form_post,
                    form_post1 = form_post,
                    form_post2 = form_post,
                    form_post3 = form_post,
            )
            )
        else:
            find_objs_str = ('{model_name}.objects.all()'
                             '[{start_pos}:{end_pos}]'.format(
                    model_name=model_name,
                    start_pos=start_pos,
                    end_pos=end_pos)
            )

        objs = eval(find_objs_str)#eval() 函数可将字符串转换为代码执行，并返回一个或多个值

        # 计算总共的页数
        if form_post is not None:
            find_objs_count_str = '{model_name}.objects.filter(Q(jobname__contains="{form_post3}")|Q(date__contains="{form_post2}")|Q(address__contains="{form_post}")|Q(jobname__contains="{form_post1}")).count()'.format(
                    model_name = model_name,form_post = form_post,form_post1 = form_post,form_post2 = form_post,form_post3 = form_post)
            all_obj_counts = eval(find_objs_count_str)
            all_page = all_obj_counts / one_page_data_size
            remain_obj = all_obj_counts % one_page_data_size
            if remain_obj > 0:
                all_page += 1
        else:
            find_objs_count_str = '{model_name}.objects.count()'.format(
                        model_name=model_name)
            all_obj_counts = eval(find_objs_count_str)
            all_page = all_obj_counts / one_page_data_size
            remain_obj = all_obj_counts % one_page_data_size
            if remain_obj > 0:
                all_page += 1

        # 限制当前页不能小于1和并且大于总页数
        cur_page = 1 if cur_page < 1 else cur_page
        cur_page = all_page if cur_page > all_page else cur_page

        # 获得显示页数的最小页
        start_page = cur_page - show_page_item_len / 2
        if start_page > all_page - show_page_item_len:
            start_page = all_page - show_page_item_len + 1
        start_page = 1 if start_page < 1 else start_page

        # 获得显示页数的最大页
        end_page = cur_page + show_page_item_len / 2
        end_page = all_page if end_page > all_page else end_page
        if end_page < show_page_item_len and all_page > show_page_item_len:
            end_page = show_page_item_len

        # 获得上一页
        pre_page = cur_page - 1
        pre_page = 1 if pre_page < 1 else pre_page

        # 获得下一页
        next_page = cur_page + 1
        next_page = all_page if next_page > all_page else next_page

        # 处理省略符，是否显示
        if start_page <= 1:
            start_page_omit_symbol = ''

        if end_page >= all_page:
            end_page_omit_symbol = ''

        # 创建能点击的展示页码
        page_items = range(int(start_page), int(end_page + 1))#python3 range范围float报错
        pagination = {
            'objs': objs,
            'all_obj_counts': int(all_obj_counts),
            'start_pos': int(start_pos),
            'end_pos': int(end_pos),
            'all_page': int(all_page),
            'cur_page': int(cur_page),
            'pre_page': int(pre_page),
            'next_page': int(next_page),
            'page_items': page_items,
            'start_page_omit_symbol': start_page_omit_symbol,
            'end_page_omit_symbol': end_page_omit_symbol,
        }
        return pagination