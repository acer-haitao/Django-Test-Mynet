from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from guestbook import models
import datetime
# Create your views here.

#提取留言显示
def comment(request):
    messages = models.Msg.objects.filter().order_by('-id')
    return render(request,'comment.html',context={'messages':messages})

#转到留言界面
def create(request):
    return render(request, 'create.html')

#接收留言
def save(request):
    username = request.POST.get('username')
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = request.POST.get('title')
    txt = request.POST.get('content')
    message = models.Msg(username=username,time=time,title=title,txt=txt)
    message.save()
    return HttpResponseRedirect('/comment/')

#删除留言
def delete(request):
    return render(request,'delete.html')

def deleteid(request):
    pwd = request.POST.get('pwd')
    id = request.POST.get('ID')
    if pwd == '12345':
        test = models.Msg.objects.get(id=int(id))
        str ={}
        str = "ID号:%s--时间:%s--内容:%s"%(test.id,test.time,test.txt)
        test.delete()
        return HttpResponse(str)
    else:
        return HttpResponse("删除失败")
    return HttpResponseRedirect('/comment/')