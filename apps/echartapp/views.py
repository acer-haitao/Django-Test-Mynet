# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import math

import MySQLdb
from django.shortcuts import render
from django.template import loader
from pyecharts import Line3D
from pyecharts.constants import DEFAULT_HOST
# 将数据库数据在Web页面展示
from .models import PageViewStatistics
from apps.job51.models import job51

def jobWages(jobnamestr):
    # 职位总数
    job_count = job51.objects.filter(jobname=jobnamestr).count()
    # 根据岗位和工资筛选
    job_wages = job51.objects.filter(jobname=jobnamestr).values_list('wages', flat=True)
    hist = {}
    for word in job_wages:
        if word not in hist:  # 生成列表并统计个数
            hist[word] = 1
        else:
            hist[word] = hist[word] + 1
    # 字典排序
    hist_sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)
    # 将key和value分开
    hist_wages = []
    hist_wages_count = []
    for k, v in hist_sort:
        hist_wages.append(k)
        hist_wages_count.append(v)
    data = [job_count, hist_wages, hist_wages_count]
    return data


def jobAddress(jobnamestr):
    # 职位总数
    job_count = job51.objects.filter(jobname=jobnamestr).count()
    # 区域列表
    job_adresss = job51.objects.filter(jobname=jobnamestr).values_list('address', flat=True)
    hist = {}
    for word in job_adresss:
        if word not in hist:  # 生成列表并统计个数
            hist[word] = 1
        else:
            hist[word] = hist[word] + 1
    # 字典排序
    hist_sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)
    # 将key和value分开
    hist_address = []
    hist_address_count = []
    for k, v in hist_sort:
        hist_address.append(k)
        hist_address_count.append(v)
    data =[job_count,hist_address,hist_address_count]
    return data

def getkv_dict_all(jobnamestr,sqlchoice):
    """
    :param jobnamestr:职位名称--python、C#、java
    :param sqlchocie: 数据库筛选字段比如工资、地点、日期、公司
    :return:构造成[{'name': '武汉', 'value': 2513}, {'name': '武汉-洪山区', 'value': 1531}...]
    """
    # 职位总数
    job_count = job51.objects.filter(jobname=jobnamestr).count()
    # 区域列表
    job_adresss = job51.objects.filter(jobname=jobnamestr).values_list(sqlchoice, flat=True)

    hist = {}
    for word in job_adresss:
        if word not in hist:  # 生成列表并统计个数
            hist[word] = 1
        else:
            hist[word] = hist[word] + 1
    # 字典排序
    hist_sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)
    # 将key和value分开
    data = []
    for k, v in hist_sort:
        tmp = {'name': k, 'value': v}
        data.append(tmp)
    # 将key和value分开
    hist_address = []
    hist_address_count = []
    for k, v in hist_sort:
        hist_address.append(k)
        hist_address_count.append(v)
    data_all = [job_count,hist_address,hist_address_count,data]#获取全部数据

    return data_all

def getkv_dict(jobnamestr):
    """
    主要为饼图数据准备:[{'name': '武汉', 'value': 2513}, {'name': '武汉-洪山区', 'value': 1531}...]
    """
    # 职位总数
    job_count = job51.objects.filter(jobname=jobnamestr).count()
    # 区域列表
    job_adresss = job51.objects.filter(jobname=jobnamestr).values_list('address', flat=True)
    hist = {}
    for word in job_adresss:
        if word not in hist:  # 生成列表并统计个数
            hist[word] = 1
        else:
            hist[word] = hist[word] + 1
    # 字典排序
    hist_sort = sorted(hist.items(), key=lambda x: x[1], reverse=True)
    # 将key和value分开
    data =[]
    for k, v in hist_sort:
        tmp={'name':k,'value':v}
        data.append(tmp)
    return data

def jobAnalysis(request):
    data_wage_bj = jobWages("BJJSZC")
    data_wage_wh = jobWages("WHJSZC")

    data = jobAddress("WHJSZC")
    data_bj = jobAddress("BJJSZC")

    data_pie_wh = getkv_dict("WHJSZC")
    data_pie_bj = getkv_dict("BJJSZC")

    jobnamestr = "WHJSZC"
    sqlchoice = "wages"
    data_wh_wage_pie = getkv_dict_all(jobnamestr,sqlchoice)

    jobnamestr = "BJJSZC"
    sqlchoice = "wages"
    data_bj_wage_pie = getkv_dict_all(jobnamestr, sqlchoice)

    return render(request,'echartapp/jobAnalysis.html',
                  {
                      'jobcount':data[0],
                      'address':data[1],
                      'address_count':data[2],

                      'jobcount_bj':data_bj[0],
                      'address_bj':data_bj[1],
                      'address_count_bj':data_bj[2],

                      'pie_wh':data_pie_wh,
                      'pie_bj':data_pie_bj,

                      'pie_wh_wage': data_wh_wage_pie[3][0:25],
                      'pie_wh_wagename':data_wh_wage_pie[1][0:25],

                      'pie_bj_wage': data_bj_wage_pie[3][0:25],
                      'pie_bj_wagename': data_bj_wage_pie[1][0:25],

                      'wage_count_wh':data_wage_wh[0],
                      'wage_name_wh':data_wage_wh[1],
                      'wage_wh':data_wage_wh[2],

                      'wage_count_bj': data_wage_bj[0],
                      'wage_name_bj': data_wage_bj[1],
                      'wage_bj': data_wage_bj[2],
                  }
                  )

def connect_mysql(sql):
    connect = MySQLdb.connect('mysql.litianqiang.com', 'novel', 'qiangzi()', 'test', port=7150, charset="utf8")
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        connect.close()
        return result
    except Exception as e:
        print("SQLERRO", e)
        connect.close()
        pass

def hdd(request):
    sql = "select price,sold from hduoduo order by price ASC ;"
    result = connect_mysql(sql)
    price = []
    sold = []
    for tmp in result:
        price.append(tmp[0])
        sold.append(tmp[1])
    return render(request,'echartapp/hdd.html',context={'price':json.dumps(price),'sold':json.dumps(sold)})

def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', 
                   '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', 
                   '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=range_color,
            visual_range=[0, 30], is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d


def pyechart3d(request):
    '''使用pycharts绘图，使用html5进行渲染...'''
    template = loader.get_template('echartapp/pycharts.html')
    l3d = line3d()
    context = dict(myechart=l3d.render_embed(),
            host=DEFAULT_HOST,
            script_list=l3d.get_js_dependencies()
            )
    # return HttpResponse(template.render(context, request))
    return render(request, 'echartapp/pycharts.html', context)

def linechart(request):
    ''' 绘制折线图... '''
    return render(request, 'echartapp/linechart.html')

def dev(request):
    ''' 绘制折线图... '''
    sql = "select uptime,dev_float from devapp_dev_data; "
    line_test = connect_mysql(sql)
    up = []
    dev_float = []
    for tmp in line_test:
        up.append(tmp[0])
        dev_float.append(tmp[1])
    return render(request, 'echartapp/dev.html', context={"uptime":json.dumps(up), "dev_float":json.dumps(dev_float)})

def multilinechart(request):
    ''' 绘制多维折线图... '''
    pv_statistics = dict()
    datalist = list(PageViewStatistics.objects.values("view_way", "page_views"))
    print(datalist)
    for item in datalist:
        key = item['view_way']
        value = item['page_views']
        if key in pv_statistics.keys():
            (pv_statistics[key]).append(value)
        else:
            pv_statistics[key] = [value]
    print(pv_statistics)
    context = {'data_dict': pv_statistics}
    return render(request, 'echartapp/multilinechart.html', context=context)

def barchart(request):
    ''' 绘制柱状图 '''
    return render(request, 'echartapp/barchart.html')

def piechart(request):
    return render(request, 'echartapp/piechart.html')
