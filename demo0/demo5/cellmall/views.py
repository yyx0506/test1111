from django.shortcuts import render, reverse, redirect
from .models import User,Userinfo

# Create your views here.
def index(request):
    return render(request, "cellmall/indexes.html")
def register(request):
    if request.method=="GET":
        return render(request,"cellmall/register.html")
    elif request.method=="POST":
        account=request.POST.get("account")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        result=User.objects.ifregest(account,password,password2)
        if result=="注册成功":
            name=request.session.get("account")
            return redirect("cellmall:login")
        else:
            return render(request,"cellmall/register.html")

def login(request):
    if request.method == "GET":
        return render(request, 'cellmall/login.html')
    elif request.method == "POST":
        request.session['username'] = request.POST["username"]
        return redirect("cellmall/indexes.html")
def logout(request):
    request.session.clear()
    return redirect("cellmall/indexes.html")
