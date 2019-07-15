from django.db import models

# Create your models here.
class Typeinfo(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Goodsinfo(models.Model):
    title=models.CharField(max_length=20)
    pic=models.ImageField(upload_to="df_goods") #商品图片
    price=models.DecimalField(max_digits=5,decimal_places=2)# 单价
    danwei=models.CharField(max_length=20,default="500g") # 单位
    goodsclick=models.IntegerField(default=0) #点击量  人气
    goodstype=models.ForeignKey(Typeinfo) #类型
    goodsdetail=models.CharField(max_length=50)  #商品简介
    goodscontent=models.TextField()  #商品详情
    def __str__(self):
        return self.title
# class


