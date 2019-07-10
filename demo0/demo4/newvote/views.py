from django.shortcuts import render,redirect,reverse
from .models import *
from .form import LoginForm,RegistForm
# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login as loi ,logout as lot,authenticate

def checklogin(fun):
    def checklog(request,*args):
        #使用cookie
        # username = request.COOKIES.get('username')
        #使用session
        # username = request.session.get('username')
        # username=request.POST.get()
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse("newvote:login"))
    return checklog

def logout(request):
    #删除使用cookie
    # print(dir(request.COOKIES))
    # res=redirect(reverse("newvote:login"))
    # res.delete_cookie('username')
    # return res
    #删除使用session
    # request.session.flush()
    #使用授权模块
    lot(request)
    return redirect(reverse("newvote:login"))
def regist(request):
    form=LoginForm()
    rgf=RegistForm()
    if request.method == 'GET':
        return render(request, "newvote/login.html", locals())
    elif request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            user=rgf.save(commit=False)
            user.set_password(rgf.cleaned_data["password"])
            user.save()
            return redirect(reverse("newvote:login"))
        else:
            return render(request, 'newvote/login.html', {'erros': '注册失败'},locals())
    # if request.method =="POST":
    #     username=request.POST.get("username")
    #     password=request.POST.get("password")
    #     try:
    #         user=MyUser.objects.create_user(username=username,password=password)
    #     except :
    #         user=None
    #     if user:
    #         return redirect(reverse("newvote:login"))
    #     else:
    #         return render(request,'newvote/login.html',{'erros':'注册失败'})
def login(request):
    form=LoginForm()
    rgf=RegistForm()
    if request.method == 'GET':
        return render(request,"newvote/login.html",locals())
    elif request.method == 'POST':
        #表单类自建
        lgf = LoginForm(request.POST)
        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                loi(request,user)
                return redirect(reverse("newvote:index"))
            else:
                return render(request,"newvote/login.html",{'erros':'登录失败'},locals())
        #使用cookie
        # responce=redirect(reverse("newvote:index"))
        #使用session
        # responce.set_cookie("username",request.POST.get("username"))
        # return responce
        # username=request.POST.get('username')
        # password=request.POST.get('password')


        #判断是否登陆成功授权
        # try:
        #     user = authenticate(request, username=username, password=password)
        # except  :
        #     user=None

        # request.session['username']=request.POST.get("username")
        # return redirect(reverse("newvote:index"))

@checklogin
def index(request):
    question = Question.objects.all()
    username=request.user
    return render(request, "newvote/index.html", locals())
    # print(request.user,request.user.is_authenticated)
    # user=MyUser.objects.create_user(username='yyx',email="154564565412@qq.com",password="123")
    # print(user,user.is_authenticated)
    # if user:
    #     print(user,user.is_authenticated)
    #     loi(request,user)
    #     print(request.user, request.user.is_authenticated)
    #     lot(request)
    #     print(request.user, request.user.is_authenticated)
    #使用cookie
    # username = request.COOKIES.get('username')
    #使用session
    # username=request.session.get('username')

@checklogin
def list(request,id):
    question=Question.objects.get(pk=id)
    if request.method=='GET':
        return render(request,"newvote/list.html",locals())
    elif request.method == 'POST':
        vote=request.POST.get("cc")
        new=Chioce.objects.get(pk=vote)
        new.votes+=1
        new.save()
        return redirect(reverse("newvote:result",args=(question.id,)))
@checklogin
def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"newvote/result.html",locals())

#添加新的投票信息
@checklogin
def newquestion(request):
    if request.method == 'GET':
        return render(request,'newvote/newquestion.html')
    elif request.method == 'POST':
        newquestion = request.POST.get("newquestion")
        n1=Question()
        n1.question=newquestion
        n1.save()
        return redirect(reverse("newvote:index"))
#添加新的投票选择
@checklogin
def addchouse(request,id):
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'newvote/addchouse.html',{"question":question})
    elif request.method == 'POST':
        newquestion = request.POST.get("addchouse")
        n1=Chioce()
        n1.chioce=newquestion
        n1.name=question
        n1.save()
        return redirect(reverse('newvote:list',args=(question.id,)))