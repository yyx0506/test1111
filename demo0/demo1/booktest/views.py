from django.shortcuts import render,redirect,reverse
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Bookinfo,HeroInfo,HeroInfoManage,Ads
from django.views.generic import View,ListView


class Addimg(View):
    def get(self,request):
        # return  HttpResponse('打开上传页面')
        return render(request,"booktest/addimg.html")
    def post(self,request):
        ads=Ads()
        ads.title=request.POST.get('title')
        ads.img=request.FILES['addimg']
        ads.save()
        return  HttpResponse('上传成功')

#自定义视图函数   绑定路由
def index(request):
    ads=Ads.objects.all()
    return render(request,"booktest/index.html",{"username":"yyx",'ads':ads})

class Listview(ListView):
    model = Bookinfo
    template_name = "booktest/list.html"
    context_object_name = "books"
    def queryset(self):
        return Bookinfo.objects.all()
#返回渲染的结果
def list(request):
    books = Bookinfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})

def detail(request,id):
    book = Bookinfo.objects.get(pk=id)
    return render(request,"booktest/result.html",{"book":book})
#重定向  两次请求  redirect 解决重定向问题  reverse解决页面跳转问题

def deletehero(request,id):
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return redirect(reverse("booktest:detail",args=(bookid,)))
def deletebook(request,id):
    book=Bookinfo.objects.get(pk=id)
    book.delete()
    return  redirect(reverse("booktest:list"))
def addhero(request,id):
    # book
    book=Bookinfo.objects.get(pk=id)
    if request.method=='GET':
        return render(request,"booktest/addhero.html",{'book':book})
    elif request.method=='POST':
        name=request.POST.get("username")
        content=request.POST.get("content")
        gender= request.POST.get("gender")
        HeroInfo.object.addhero(name,content,book,gender)

        return redirect(reverse("booktest:detail",args=(id,)))















    # temp1 = loader.get_template("booktest/result.html")
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