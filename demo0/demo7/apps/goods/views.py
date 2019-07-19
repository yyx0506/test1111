from django.shortcuts import render,reverse,redirect
from django.views import View
from django.core.paginator import Paginator, Page
from .models import *
from sellfresh.views import checklogin
from django.http import HttpResponse
from sellfresh.models import Comment
# Create your views here.
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
#商品详情并用COOKIES临时存储值
class Detail(View):
    def get(self,request,id):
        username=request.user
        good=Goodsinfo.objects.get(pk=id)
        good.goodsclick+=1
        good.save()
        type = good.goodstype
        news = type.goodsinfo_set.order_by('-id')[0:2]
        responce=render(request,"sellfresh/detail.html",locals())
        good_ids=request.COOKIES.get("good_ids","")
        good_id='%d'%good.id
        if good_ids != '':
            good_ids1=good_ids.split(",")
            if good_ids1.count(good_id) >= 1:
                good_ids1.remove(good_id)
            good_ids1.insert(0,good_id)
            if len(good_ids1) >= 6:
                del good_ids1[5]
            good_ids=",".join(good_ids1)
        else :
            good_ids=good_id
        responce.set_cookie("good_ids",good_ids)
        return responce
    @checklogin
    def post(self,request):
        pass
#分类列表全显示
class List(View):
    def get(self,request,id,choose):
        username=request.user
        typeop=TypeInfo.objects.get(pk=id)
        #新品推荐最新的两个物品
        news=typeop.goodsinfo_set.order_by('-id')[0:2]
        #选择不同按钮的到不同的列表排序
        if choose == '1':
            goods=Goodsinfo.objects.filter(goodstype=id)
        elif choose == '2':
            goods=Goodsinfo.objects.filter(goodstype=id).order_by('price')
        elif choose == '3':
            goods=Goodsinfo.objects.filter(goodstype=id).order_by('-price')
        else :
            goods = Goodsinfo.objects.filter(goodstype=id).order_by('-goodsclick')
        #对所有的物品进行分页处理
        page, left_has_more, right_has_more = getpage(request, goods, 1)
        return render(request,"sellfresh/list.html",locals())
    def post(self):
        pass
#商品的评价
class GoodComment(View):
    def get(self,request,id):
        good=Goodsinfo.objects.get(pk=id)
        allcomment=good.comment_set.all()
        return redirect(reverse("goods:commnet",locals()))
    def post(self,request,id):
        pass
