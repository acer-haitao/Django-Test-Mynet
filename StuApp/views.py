from django.shortcuts import render
from StuApp.models import URLDB
from StuApp.models import TabName
from collections import ChainMap

# Create your views here.

def index(request):
    li_dict = ChainMap()

#    for list_num in range(21,22):
#        li_list_tab = {'tab1','tab2','tab3','tab4','tab5','tab6','tab7','tab8','tab9','tab10','tab11','tab12','tab13'}
#        li_dict["tab%s"%(list_num)] = li_list_tab
#       li_dict = li_dict.new_child()
#       li_dict.parents

#    for list_num in range(1,13):
#       li_list = URLDB.objects.filter(Num=list_num)
#        li_dict["tab%s"%(list_num)] = li_list
#        li_dict = li_dict.new_child()
#        li_dict.parents
#        print(dict(li_dict))
#    return render(request,"right.html",context= dict(li_dict))

    for num in range(1,13):
        url_name = URLDB.objects.filter(Num=num)
        li_dict['tab%s'%(num)] = url_name
        li_dict = li_dict.new_child()
        li_dict.parents
    #li_dict['test'] =[ i[0] for i in dict(li_dict).items()]
    li_dict['test'] = sorted(dict(li_dict).items())#将chainmap的li_dict经过dict转换成字典 转换成items是为了取key，value值 sorted排序
    li_dict =li_dict.new_child()
    li_dict.parents
    print(dict(li_dict))

    return render(request, "right.html", context=dict(li_dict))