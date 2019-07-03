from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#自定义视图函数   绑定路由
def index(request):
    return HttpResponse("这是一个首页  <div style='height:100px;width:100px;background-color:red'><a href='/list/'>跳转到列表页</a></div>")
def list(request):
    s="""
    <br>
    <a href='/detail/1/'>跳转到详情页1</a>
    <br>
    <a href='/detail/2/'>跳转到详情页2</a>
    <br>
    <a href='/detail/3/'>跳转到详情页3</a>
    """
    return HttpResponse("这是一个列表页%s"%(s,))
def detail(request,id):
    return HttpResponse("这是一个%s详情页 <a href='/'>跳转到首页</a>"%(id,))


# def ooo(request):
#     return HttpResponse('https://blog.csdn.net/u012069883/article/details/82378295')
#
#
#
# def myview(request):
#     return HttpResponse("这是一个自定义路由")
#
# def youview(request):
#     return HttpResponse("这是你的自定义路由")