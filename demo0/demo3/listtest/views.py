from django.shortcuts import render,redirect,reverse
from .models import Question,Choice
from django.http import HttpResponse

from django.views.generic import View,ListView
# Create your views here.

#展示所有信息
def index(request):
    list = Question.objects.all()
    context = {'list': list}
    return render(request, 'listtest/indexes.html', context)
#查看问题的选择答案
def list(request, id):
    question = Question.objects.get(pk=id)
    # vvot=question.choice_set.all()
    if request.method == 'GET':
        return render(request, 'listtest/list.html', {'question': question})
    elif request.method == 'POST':
        name = request.POST.get("choice")
        id=Choice.objects.get(pk=name)
        # id.votes += 1
        id.incresvotes()
        id.save()
        return redirect(reverse("listtest:result", args=(question.id,)))
# #展示相应的投票具体信息
def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request, 'listtest/result.html', {'question': question})
#添加新的投票信息
def newquestion(request):
    if request.method == 'GET':
        return render(request,'listtest/newbook.html')
    elif request.method == 'POST':
        newquestion = request.POST.get("newquestion")
        n1=Question()
        n1.question_text=newquestion
        n1.save()
        return redirect(reverse("listtest:indexes"))
#添加新的投票选择
def addchouse(request,id):
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'listtest/addhero.html',{"question":question})
    elif request.method == 'POST':
        newquestion = request.POST.get("addchouse")
        n1=Choice()
        n1.choice_text=newquestion
        n1.question=question
        print(n1.choice_text)
        n1.save()
        # return render(request, 'listtest/list.html', {'question': question})
        return redirect(reverse('listtest:list',args=(question.id,)))