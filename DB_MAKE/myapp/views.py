from django.shortcuts import render
from myapp.models import *


# Create your views here.

def home(request):
    all_links = DB_links.objects.all()  # 获取所有链接
    list_all_links = list(all_links.values())
    return render(request, 'home.html', {"all_links": list_all_links})  # 在首页显示
