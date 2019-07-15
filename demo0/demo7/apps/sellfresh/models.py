from django.db import models
from django.contrib.auth.models import User
from goods.models import Goodsinfo
# Create your models here.
class Myuser(User):
    telephone=models.CharField(max_length=11)

# class Cart(models.Model):
#     goods=models.ForeignKey(Goodsinfo)
#     goodsprice=models.DecimalField(max_digits=8,decimal_places=2)
#     goodsnumber=models.IntegerField()
#     updatetime=models.DateTimeField(auto_now=True)
#
#
# class Comment(models.Model):
#     author=models.ForeignKey(Myuser)
#     commenttime=models.DateTimeField(auto_now_add=True)
#     comment=models.TextField()
#
# class Order(models.Model):
#     pass

