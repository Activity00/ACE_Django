#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

def index(request):
    #基本元素切换导入
    return render(request, 'mytemp/mainpage.html')

def index2(request):
    return render(request, 'mytemp/mainpage2.html')