from django.shortcuts import render,reverse,redirect
from .models import Book,Hero

# Create your views here.
def index(request):
    return render(request,"herotest/index.html",{"username":"杨超越"})
def list(request):
    bookinfo=Book.objects.all()
    return render(request,"herotest/list.html",locals())
def detail(requset,id):
    book = Book.objects.get(pk=id)
    return render(requset,"herotest/detail.html",locals())
def heroinfo(requset,id):
    hero =Hero.objects.get(pk=id)
    return render(requset,"herotest/heroinfo.html",locals())
def deletebook(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect(reverse("herotest:list"))
def deletehero(request,id):
    hero=Hero.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    return redirect(reverse("herotest:detail",args=(bookid,)))
def newbook(request):
    if request.method=="GET":
        return render(request,"herotest/newbook.html")
    elif request.method=="POST":
        newbookname= request.POST.get("newbook")
        Book.objects.addbook(newbookname)
        return redirect(reverse("herotest:list"))
def addhero(request,id):
    book=Book.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"herotest/addhero.html",locals())
    elif request.method=="POST":
        newheroname= request.POST.get("heroname")
        newherocontent=request.POST.get("content")
        newherogender=request.POST.get("gender")
        Hero.objects.addhero(newheroname, newherocontent, book, newherogender)
        return redirect(reverse("herotest:detail",args=(book.id,)))


