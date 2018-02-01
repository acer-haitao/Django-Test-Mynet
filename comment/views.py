from django.shortcuts import render
from comment import models
# Create your views here.
def net163(request):
    comment = models.comment.objects.all()
    return render(request,'Net163.html',context={'comment':comment})
