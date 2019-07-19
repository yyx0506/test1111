from django.shortcuts import render
from .models import Newbook
def index(request):
    return render(request,"newbook/indexes.html",{"username":"杨超越"})
def list(request):
    books = Newbook.objects.all()
    return render(request,"newbook/list.html",{"books":books})
def detail(request,id):
    book = Newbook.objects.get(pk=id)
    return render(request,"newbook/result.html",{"book":book})