# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 11:14
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : pdf.py
# @Software: PyCharm
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from urllib.request import urlopen
from  reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

'''--- 注册字体 ---'''
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))  # 注册要使用的字体

'''--- 获取数据 ---'''
data = []
for line in urlopen(r'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'):  # 打开在线文件并循环读取每一行
    line = line.decode('ascii')  # 读取到的内容需要进行解码
    if line[0] not in [':', '#']:  # 判断首位字符不是指定字符之一
        data.append(line.split())  # 以逗号分隔每行内容并添加到列表

'''--- 创建画布 ---'''
draw = Drawing(400, 240)

'''--- 创建各条线段数值（默认将数值做为y轴坐标）列表和x轴时间列表 ---'''
predict = [float(row[2]) for row in data]  # 创建预测线数值列表
high = [float(row[3]) for row in data]  # 创建最高线数值列表
low = [float(row[4]) for row in data]  # 创建最低线数值列表
times = [float(row[0]) + float(row[1]) / 12 for row in data]  # 创建时间轴数值列表

'''--- 创建图表 ---'''
chart = LinePlot()

chart.data = [tuple(zip(times, predict)), tuple(zip(times, high)), tuple(zip(times, low))]  # 混合列表数据添加到图表
chart.lines[0].strokeColor = colors.green  # 设置预测线颜色
chart.lines[1].strokeColor = colors.red  # 设置最高线颜色
chart.lines[2].strokeColor = colors.blue  # 设置最低线颜色
chart.width = 320  # 设置图表宽度
chart.height = 180  # 设置图表高度
chart.x = 40  # 设置图表整体x轴坐标
chart.y = 30  # 设置图表整体y轴坐标
chart.xValueAxis.valueStep = 1  # 设置图表时间轴步进间隔

'''--- 创建标题 ---'''
title = String(200, 220, '太阳黑子活动信息图')  # 创建文本对象
title.fontName = 'msyh'  # 设置文本字体
title.fontSize = 14  # 设置文本字号
title.fillColor = colors.gray  # 设置文本颜色
title.textAnchor = 'middle'  # 设置文本位置的锚点

'''--- 添加图表与标题到画布并生成PDF文件 ---'''
draw.add(chart)
draw.add(title)
renderPDF.drawToFile(draw, 'chart02.pdf', '太阳黑子活动信息')