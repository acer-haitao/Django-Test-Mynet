from django.shortcuts import render

# Create your views here.
def arcticle(request):
    return render(request,"article.html")