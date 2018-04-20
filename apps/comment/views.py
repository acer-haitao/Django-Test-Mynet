from django.shortcuts import render

from apps.comment.pageshow import Pagination#分页

# Create your views here.
cur_page = 1
def net163(request):
    global cur_page#处理报错local variable 'cur_page1' referenced before assignment
    try:
        #cur_page = int(request.GET.get('cur_page', '1'))#跳转页码
        if request.POST:
            cur_page = int(request.POST['num'])
        elif request.GET:
            cur_page = int(request.GET['cur_page'])
        else:
            cur_page = 1
    except ValueError:
        cur_page = 1
    #自定义分页类
    pagination = Pagination.create_pagination(
            from_name='apps.comment.models',
            model_name='comment',
            cur_page=cur_page,
            start_page_omit_symbol='...',
            end_page_omit_symbol='...',
            one_page_data_size=30,#每页显示数目
            show_page_item_len=10)#分页数目
    return render(request, 'Net163.html', {'pagination': pagination})