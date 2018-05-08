from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from apps.job51 import views as job_views
from apps.StuApp import views as ht_index
from apps.guestbook import views as guest_views
from apps.comment import views as net163_views
from apps.echartapp import views
from apps.app01 import views as app01views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^deleteid',guest_views.deleteid),
    url(r'^delete',guest_views.delete),
    url(r'^save/',guest_views.save),
    url(r'^create',guest_views.create),
    url('^comment/',guest_views.comment),
    url(r'^net163', net163_views.net163),
    url(r'^job/$',job_views.job),
    url(r'^txt/$', job_views.txt),
    url(r'^search',include('haystack.urls')),
    url(r'^pychart3d/$', views.pyechart3d, name='pychart3d'),
    # 使用 echarts.js  渲染，并在 Web 页面展示折线图...
    url(r'^linechart/$', views.linechart, name='linechart'),
    url(r'^dev/$', views.dev, name='linecharttest'),
    # 使用 echarts.js 渲染，并在 Web 页面展示多维折线图...
    url(r'^multilinechart/$', views.multilinechart, name='multilinechart'),
    url(r'^hdd/$', views.hdd, name='linecharthdd'),
    # 柱状图
    url(r'^barchart/$', views.barchart, name='barchart'),
    # 饼状图
    url(r'^piechart/$', views.piechart, name='piechart'),
    url(r'^index1/$', ht_index.index1, name='index1'),
    url(r'^article/',app01views.arcticle,name='article'),
    url(r'^Analysis/',views.jobAnalysis,name='Analysis'),
    url(r'^PieAnalysis/', views.PieAnalysis, name='PieAnalysis'),
    url(r'^jobdelete/$', job_views.jobdelete, name='jobdelete'),
    url(r'', ht_index.index, name='index'),
]
