from django.shortcuts import render
from job51 import pageshow

# Create your views here.

cur_page = 1
form_post = "python"
def job(request):
    global cur_page
    global form_post
    #自定义分页类
    try:
        # cur_page = int(request.GET.get('cur_page', '1'))#跳转页码
        if request.POST:
            form_post = request.POST['key']
            #form_adress = request.POST['adress']
            #print(form_adress)
        elif request.GET:
            cur_page = int(request.GET['cur_page'])
        else:
            print("数据传输有误")
    except ValueError:
        cur_page = 1
    pagination = pageshow.Pagination.create_pagination(
            from_name='job51.models',
            model_name='job51',
            cur_page=cur_page,
            start_page_omit_symbol='...',
            end_page_omit_symbol='...',
            one_page_data_size=30,#每页显示数目
            show_page_item_len=10,
            form_post = form_post,
    )#分页数目
    #print(pagination)
    return render(request,"job.html",{'pagination': pagination})