from django.shortcuts import render

from apps.job51 import pageshow

# Create your views here.

cur_page = 1
form_post = "python"
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