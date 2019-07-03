from django.shortcuts import render
# from django.template import loader
# Create your views here.
# from django.http import HttpResponse
from .models import Bookinfo,HeroInfo
#自定义视图函数   绑定路由
def index(request):
    return render(request,"booktest/index.html",{"username":"yyx"})
    # return HttpResponse("这是一个首页  <div style='height:100px;width:100px;background-color:red'><a href='/list/'>跳转到列表页</a></div>")
    # temp1=loader.get_template("booktest/index.html")
    # #获取魔板
    # result=temp1.render({})
    # #渲染字典参数
    # return HttpResponse(result)
#返回渲染的结果
def list(request):
    books = Bookinfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})
    # temp1=loader.get_template("booktest/list.html")
    # result=temp1.render({"books":books})
    # return HttpResponse(result)
    # return HttpResponse("这是一个列表页%s"%(s,))
def detail(request,id):
    book = Bookinfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})














    # temp1 = loader.get_template("booktest/detail.html")
    # print(id)
    # result = temp1.render({'book':book})
    # return HttpResponse(result)
    # return HttpResponse("这是一个%s详情页 <a href='/'>跳转到首页</a>"%(id,))








# def ooo(request):
#     return HttpResponse('https://blog.csdn.net/u012069883/article/details/82378295')

# def myview(request):
#     return HttpResponse("这是一个自定义路由")
#
# def youview(request):
#     return HttpResponse("这是你的自定义路由")