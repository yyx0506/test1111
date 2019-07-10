from django.shortcuts import render,redirect,reverse

# Create your views here.
def blog(request):
    return render(request,"blog/index.html")
def single(request):
    return render(request,"blog/single.html")
