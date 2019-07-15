from django.db import models
from blog.models import Artical
# Create your models here.
class Comment(models.Model):
    artical=models.ForeignKey(Artical,on_delete=True)
    author=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    email=models.EmailField(blank=True,null=True)
    url=models.URLField(blank=True,null=True,default="http://www.baidu.com")
    body=models.TextField()