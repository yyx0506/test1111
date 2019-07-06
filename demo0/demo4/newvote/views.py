from django.shortcuts import render,redirect,reverse
from .models import *
# Create your views here.
def index(request):
    question=Question.objects.all()
    return render(request,"newvote/index.html",locals())
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
def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"newvote/result.html",locals())

#添加新的投票信息
def newquestion(request):
    if request.method == 'GET':
        return render(request,'newvote/newbook.html')
    elif request.method == 'POST':
        newquestion = request.POST.get("newquestion")
        n1=Question()
        n1.question=newquestion
        n1.save()
        return redirect(reverse("newvote:index"))
#添加新的投票选择
def addchouse(request,id):
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'newvote/addhero.html',{"question":question})
    elif request.method == 'POST':
        newquestion = request.POST.get("addchouse")
        n1=Chioce()
        n1.chioce=newquestion
        n1.name=question
        n1.save()
        return redirect(reverse('newvote:list',args=(question.id,)))