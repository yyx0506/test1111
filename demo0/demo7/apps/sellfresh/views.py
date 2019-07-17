
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Myuser,Address,Cart,Order
from django.views import View
from .form import RegistForm,LoginForm,FormAddress
from django.core.paginator import Paginator, Page
# Create your views here.
from django.contrib.auth import login as loi, logout as lot, authenticate
import random,io
from PIL import Image,ImageDraw,ImageFont
from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import cache_page
from goods.models import *
#主页面的显示
class Index(View):
    def get(self,request):
        username=request.user
        ads = Ads.objects.all()
        alltype=TypeInfo.objects.all()
        return render(request,"sellfresh/index.html",locals())
    def post(self,request):
        pass

# 图片验证码功能
def verify(request):
# 定义变量， 用于画面的背景色、 宽、 高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 35
# 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
# 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
# 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    cache.set("verify",rand_str)
    print(rand_str)
    # 构造字体对象
    font = ImageFont.truetype('Arvo-Regular.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
# 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端， MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


#当账户名不对时提示
def checkuser(request):
    if request.method == "GET":
        name = request.GET.get("name")
        qs = Myuser.objects.filter(username=name)
        user = qs.first()
        if user:
            return JsonResponse({"state":1})
        else:
            return JsonResponse({"state":0,'errorinfo':"用户名不存在"})
#退出重定向到主页
def logout(request):
    lot(request)
    return redirect(reverse("sellfresh:index"))
#注册成功直接跳转到登录
def regist(request):
    form = LoginForm()
    rgf = RegistForm()
    if request.method == 'GET':
        return render(request, "sellfresh/register.html", locals())
    elif request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            user = rgf.save(commit=False)
            #对密码进行加密

            user.set_password(rgf.cleaned_data["password"])
            user.save()
            # OOlist=["yyxyanyuxiang@163.com"]
            # try:
            #     send_mail("python测试邮件","这是一封Python给你发的邮件",settings.EMAIL_HOST_USER,OOlist)
            # except Exception as e:
            #     print(e)
            return redirect(reverse("sellfresh:login"))
        else:
            return render(request, 'sellfresh/register.html', {'erros': '注册失败'}, locals())
#登录成功直接跳转到主页面
def login(request):
    form = LoginForm()
    rgf = RegistForm()
    if request.method == 'GET':
        return render(request, "sellfresh/login.html", locals())
    elif request.method == 'POST':
        # 表单类自建
        verifydode=request.POST.get('verify')
        if not verifydode == cache.get("verify"):
            return HttpResponse("验证码错误")
        lgf = LoginForm(request.POST)

        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            islogin = False
            user = authenticate(request, username=username, password=password)
            if user:
                loi(request, user)
                islogin = True
                return redirect(reverse("sellfresh:index"))
            else:
                return render(request, "sellfresh/login.html", {'erros': '登录失败'}, locals())

#对为登录的功能进行检索
def checklogin(fun):
    def checklog(self,request,*args):
        if request.user and request.user.is_authenticated:
            return fun(self,request,*args)
        else:
            return redirect(reverse("sellfresh:login"))
    return checklog
#查看商品属性
class Detail(View):
    def get(self,request,id):
        good=Goodsinfo.objects.get(pk=id)
        good.goodsclick+=1
        good.save()
        return render(request,"sellfresh/detail.html",locals())

    @checklogin
    def post(self,request,id):
        pass
class Usercenter(View):
    @checklogin
    def get(self,request):
        username=request.user
        good_ids=request.COOKIES.get("good_ids","")
        good_ids1=good_ids.split(",")
        good_list=[]
        for good_id in good_ids1:
            good_list.append(Goodsinfo.objects.get(id= int(good_id)))

        return render(request,"sellfresh/user_center_info.html",locals())
    def post(self,request):
        pass
#购物车
class Cart(View):
    @checklogin
    def get(self,request):
        username=request.user
        return render(request,"sellfresh/cart.html",locals())
    def post(self,request):
        pass
#订单
class Order(View):
    @checklogin
    def get(self,request):
        username = request.user
        return render(request, "sellfresh/user_center_order.html", locals())
    def post(self,request):
        pass
#个人地址操作
class AddAddress(View):
    @checklogin
    def get(self,request):
        username=request.user
        myuser=Myuser.objects.filter(username=username)[0]
        # print(myuser.address_set.count())
        address=FormAddress()
        return render(request,"sellfresh/user_center_site.html",locals())
    def post(self,request):
        at = get_object_or_404(Address, user=request.user)
        username = request.user
        ads = FormAddress(request.POST)
        com = ads.save(commit=False)
        com.author = at
        com.save()
        return redirect(reverse("sellfresh:address", args=(at.id,username)))
#同步加载地址
class Alladdress(View):
    def post(self,request):
        person=request.POST.get("person")
        address=request.POST.get("address")
        zip=request.POST.get("zip")
        telephone=request.POST.get("telephone")
        myuser=Myuser.objects.filter(username=request.user.username)[0]
        c=Address()
        c.person=person
        c.address=address
        c.zip=zip
        c.telephone=telephone
        c.author=myuser
        c.isdefadd="否"
        c.save()
        # a = time.localtime()
        # x = time.strftime("%Y{}-%m{}-%d{} %H:%M", (a[0], a[1], a[2], a[3], a[4], 0, 0, 0, 0)).format("年", "月", "日",)
        return JsonResponse({"person":c.person,"address":c.address,"zip":c.zip,"telephone":c.telephone})

