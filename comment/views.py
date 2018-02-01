from django.shortcuts import render
from comment.pageshow import Pagination
# Create your views here.

def net163(request):
    try:
        cur_page = int(request.GET.get('cur_page', '1'))
    except ValueError:
        cur_page = 1
    pagination = Pagination.create_pagination(
            from_name='comment.models',
            model_name='comment',
            cur_page=cur_page,
            start_page_omit_symbol='...',
            end_page_omit_symbol='...',
            one_page_data_size=10,#每页显示数目
            show_page_item_len=10)#分页数目
    return render(request, 'Net163.html', {'pagination': pagination})