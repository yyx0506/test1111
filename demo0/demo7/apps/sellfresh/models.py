from django.db import models
from django.contrib.auth.models import User
from goods.models import Goodsinfo
from DjangoUeditor.models import UEditorField
# Create your models here.
#账户信息
class Myuser(User):
    telephone=models.CharField(max_length=11)

#个人购物车
class Cart(models.Model):
    author = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    goods=models.ForeignKey(Goodsinfo, on_delete=models.CASCADE)
    goodsprice=models.DecimalField(max_digits=8,decimal_places=2)
    oneprice=models.DecimalField(max_digits=5,decimal_places=2,null=True)
    goodsnumber=models.IntegerField()
    updatetime=models.DateTimeField(auto_now=True)


#个人收货地址
class Address(models.Model):
    author = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    person=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    telephone=models.CharField(max_length=11)
    isdefadd=models.CharField(max_length=10)

#个人订单
class Order(models.Model):
    author=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    creattime=models.DateTimeField(auto_now=True)
    goods=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    ordernumber=models.CharField(max_length=10,default="000000000")
    status=models.CharField(max_length=10,default="未支付")
    allprice=models.DecimalField(max_digits=8,decimal_places=2,null=True)
    address=models.ForeignKey(Address,on_delete=True,null=True)
    pay=models.CharField(max_length=20,null=True)

#单个订单详情
class Orderinfo(models.Model):
    goods=models.ForeignKey(Goodsinfo,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    allprice=models.DecimalField(max_digits=8,decimal_places=2)
    count=models.IntegerField()


#个人评论
class Comment(models.Model):
    author=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    commenttime=models.DateTimeField(auto_now_add=True)
    orderid=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    goods=models.ForeignKey(Goodsinfo,on_delete=models.CASCADE,null=True)
    comment=UEditorField(imagePath="comment/", width="100%",null=True)
