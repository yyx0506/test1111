from django.shortcuts import render
from datetime import datetime,timedelta
import time
from .models import Comment
from blog.models import Artical
from django.http import JsonResponse
# Create your views here.
from django.views import View
class Allcommment(View):
    def post(self,request,id):
        author=request.POST.get("author")
        email=request.POST.get("email")
        url=request.POST.get("url")
        body=request.POST.get("body")
        c=Comment()
        c.author=author
        c.email=email
        c.url=url
        c.body=body
        c.artical=Artical.objects.get(pk=id)
        c.save()
        a = time.localtime()
        x = time.strftime("%Y{}-%m{}-%d{} %H:%M", (a[0], a[1], a[2], a[3], a[4], 0, 0, 0, 0)).format("年", "月", "日",)
        return JsonResponse({"author":c.author,"body":c.body,"time":x})

