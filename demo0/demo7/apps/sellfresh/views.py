
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Myuser
from django.views import View
from .form import RegistForm,LoginForm
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
#主页面的显示
class Index(View):
    def get(self,request):
        username=request.user
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

def logout(request):
    lot(request)
    return redirect(reverse("sellfresh:index"))

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
        pass
    def post(self,request,id):
        pass
class Usercenter(View):
    @checklogin
    def get(self,request):
        username=request.user
        return render(request,"sellfresh/user_center_info.html",locals())
    def post(self,request):
        pass


