from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Myuser(User):
    telephone=models.IntegerField(max_length=11)
class Ads(models.Model):
    img=models.ImageField(upload_to="static/img")
    title=models.CharField(max_length=20)
    index=models.IntegerField(max_length=11)
class Category(models.Model):
    title=models.CharField(max_length=20)
class Tag(models.Model):
    title=models.CharField(max_length=20)
class Artical(models.Model):
    title=models.CharField(max_length=20)
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    view=models.IntegerField(default=0)
    author=models.CharField(max_length=20)
    body=models.TextField()
