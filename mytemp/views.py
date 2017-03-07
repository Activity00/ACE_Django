#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.

def index(request):
    #基本元素切换导入、只包含不展开项目
    return render(request, 'mytemp/mainpage.html')

def index2(request):
    #包含展开项目
    return render(request, 'mytemp/mainpage2.html')

def ajax_deal(request):
    req=request.GET.get('req')
    return render(request,'mytemp/%s.html'%req)
