from django.shortcuts import render
from StuApp.models import URLDB
from StuApp.models import TabName
from collections import ChainMap

# Create your views here.

def index(request):
    li_dict = ChainMap()
    for num in range(1,13):
        url_name = URLDB.objects.filter(Num=num)
        li_dict['tab%s'%(num)] = url_name
        li_dict = li_dict.new_child()
        li_dict.parents
    li_dict['test'] = sorted(dict(li_dict).items())#将chainmap的li_dict经过dict转换成字典 转换成items是为了取key，value值 sorted排序
    li_dict =li_dict.new_child()
    li_dict.parents
    print(dict(li_dict))

    return render(request, "right.html", context=dict(li_dict))