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
    goodsnumber=models.IntegerField()
    updatetime=models.DateTimeField(auto_now=True)


#个人订单
class Order(models.Model):
    author=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    creattime=models.DateTimeField(auto_now=True)
    goods=models.ManyToManyField(Cart)
    ordernumber=models.CharField(max_length=10,default="000000000")
    status=models.CharField(max_length=10,default="未支付")
#个人收货地址
class Address(models.Model):
    author = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    person=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    telephone=models.CharField(max_length=11)
    isdefadd=models.CharField(max_length=10)

#个人评论
class Comment(models.Model):
    author=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    commenttime=models.DateTimeField(auto_now_add=True)
    orderid=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    goods=models.ForeignKey(Goodsinfo,on_delete=models.CASCADE,null=True)
    comment=UEditorField(imagePath="comment/", width="100%",null=True)
