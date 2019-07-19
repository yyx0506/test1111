from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Ads, Tag, Artical, Category, Myuser
from django.views import View
from .form import FormArtical, FormComment, LoginForm, RegistForm
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

# def checklogin(fun):
#     def checklog(request,*args):
#         if request.user and request.user.is_authenticated:
#             return redirect(reverse("blog:blog"))
#         else:
#             return redirect(reverse("blog:blog"))
#     return checklog
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
    return redirect(reverse("blog:blog"))
def regist(request):
    form = LoginForm()
    rgf = RegistForm()
    if request.method == 'GET':
        return render(request, "blog/login.html", locals())
    elif request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            user = rgf.save(commit=False)
            user.set_password(rgf.cleaned_data["password"])
            user.save()
            OOlist=["yyxyanyuxiang@163.com"]
            try:
                send_mail("python测试邮件","这是一封Python给你发的邮件",settings.EMAIL_HOST_USER,OOlist)
            except Exception as e:
                print(e)
            return redirect(reverse("blog:login"))
        else:
            return render(request, 'blog/login.html', {'erros': '注册失败'}, locals())
def login(request):
    form = LoginForm()
    rgf = RegistForm()
    if request.method == 'GET':
        return render(request, "blog/login.html", locals())
    elif request.method == 'POST':
        # 表单类自建
        verifydode=request.POST.get('verify')
        if not verifydode== cache.get("verify"):
            return HttpResponse("验证码错误")
        lgf = LoginForm(request.POST)
        print(dir(lgf))
        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            islogin = False
            user = authenticate(request, username=username, password=password)
            if user:
                loi(request, user)
                islogin = True
                return redirect(reverse("blog:blog"))
            else:
                return render(request, "blog/login.html", {'erros': '登录失败'}, locals())
# 分页类的实现
def getpage(request, object_list, per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    pagenum = int(pagenum)
    left_has_more = False
    right_has_more = False
    # #如果小于三就是显示...
    if pagenum > 3:
        left_has_more = True
    if (pagenum + 2) < Paginator(object_list, per_num).num_pages:
        right_has_more = True
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page, left_has_more, right_has_more


@cache_page(60)
def blog(request):
    ads = Ads.objects.all()
    art = Artical.objects.all()
    username = request.user
    # art=[]
    # for i in range(pagenum-2,pagenum+3):
    #     if i>0 and i<Paginator(art,1).num_pages:
    #         art.append(i)
    page, left_has_more, right_has_more = getpage(request, art, 1)
    return render(request, "blog/indexes.html", locals())

class Single(View):
    def get(self, request, id):
        username = request.user
        art = Artical.objects.get(pk=id)
        art.view += 1
        # art.save()
        com = FormComment()
        return render(request, "blog/single.html", locals())
    def post(self, request, id):
        at = get_object_or_404(Artical, pk=id)
        print(at)
        art = FormComment(request.POST)
        com = art.save(commit=False)
        com.artical = at
        com.save()
        return redirect(reverse("blog:single", args=(at.id,)))
# 通过年月得到不同文章
class Archives(View):
    def get(self, request, year, month):
        ads = Ads.objects.all()
        article = Artical.objects.filter(createtime__year=year, createtime__month=month)
        page, left_has_more, right_has_more = getpage(request, article, 1)
        return render(request, "blog/indexes.html", locals())
    def post(self, request):
        pass
# 通过不同的分类得到不同的文章
class Cateart(View):
    def get(self, request, id):
        ads = Ads.objects.all()
        article = Artical.objects.filter(category=id)
        page, left_has_more, right_has_more = getpage(request, article, 1)
        return render(request, "blog/indexes.html", locals())
    def post(self, request):
        pass
# 通过不同的标签得到不同的文章
class Tagart(View):
    def get(self, request, id):
        ads = Ads.objects.all()
        article = Artical.objects.filter(tag=id)
        page, left_has_more, right_has_more = getpage(request, article, 1)
        return render(request, "blog/indexes.html", locals())
    def post(self, request):
        pass
# 增加文章
class Addartical(View):
    def get(self, request):
        rgf = FormArtical()
        username = request.user
        return render(request, "blog/addartical.html", locals())
    def post(self, request):
        rgf = FormArtical(request.POST)
        if rgf.is_valid():
            art = rgf.save(commit=False)
            art.author = Myuser.objects.filter(username=request.user)[0]
            art.save()
            return redirect(reverse("blog:blog"))
        else:
          return render(request, 'blog/addartical.html', {'erros': '发布失败'}, locals())



