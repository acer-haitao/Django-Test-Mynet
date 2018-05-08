from django.shortcuts import render
from apps.job51 import models
from apps.job51 import pageshow
from django.db.models import Q
import copy
from django.views.decorators.cache import cache_page
# Create your views here.

cur_page = 1
form_post = "python"

@cache_page(60 * 15)
def job(request):
    global cur_page
    global form_post
    #自定义分页类
    try:
        if request.POST:
            form_post = request.POST['key']
        elif request.GET:
            cur_page = int(request.GET['cur_page'])
        else:
            cur_page = 1
    except ValueError:
        cur_page = 1
    if cur_page >= 1:
        pagination = pageshow.Pagination.create_pagination(
                from_name='apps.job51.models',
                model_name='job51',
                cur_page=cur_page,
                start_page_omit_symbol='...',
                end_page_omit_symbol='...',
                one_page_data_size=30,#每页显示数目
                show_page_item_len=10,
                form_post = form_post,
        )#分页数目
    else:
        pagination = pageshow.Pagination.create_pagination(
                from_name='apps.job51.models',
                model_name='job51',
                cur_page=1,
                start_page_omit_symbol='...',
                end_page_omit_symbol='...',
                one_page_data_size=30,  # 每页显示数目
                show_page_item_len=10,
                form_post=form_post,
        )  # 分页数目
    return render(request, "job.html", {'pagination': pagination})

@cache_page(60 * 15)
def txt(request):
    search_txt = 'python'
    if request.method == 'POST':
        search_txt = request.POST.get('txt')
    if search_txt:
        txt = models.job51.objects.filter(jobname=search_txt)
    else:
        txt = models.job51.objects.filter(jobname='WHJSZC')
    return render(request,'jobtxt.html',{'txt':txt})

@cache_page(60 * 15)
def jobdelete(request):
    if request.method == 'POST':
        #获取列表分类
        tmp = request.POST.get('type')

        #获取输入框输入的文本数据--日期、地点等
        data = request.POST.get('data')

        #密码验证
        pwd = request.POST.get('pwd')

        #if pwd == 'haitao':
        if True:
            print(tmp,data,pwd)
            txt = models.job51.objects.filter(Q(date=data)|Q(jobname=data)|Q(wages=data)).all()
            sum = txt.count()
            tmp = copy.copy(txt)#浅拷贝删除原始数据后现有数据不会一块删除
            txt.delete()
            return render(request, 'jobdelete.html',{'status':'1','txt':tmp,'sum':sum})
        else:
            print("pwd error")
            return render(request,'jobdelete.html',{'status':'2','pwderro':'请输入正确的密码'})
    return render(request, 'jobdelete.html', {'status': ''})
