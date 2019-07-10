from django.db import models
from blog.models import Artical
# Create your models here.
class Comment(models.Model):
    artical=models.ForeignKey(Artical,on_delete=True)
    author=models.CharField(max_length=20)
    pub_time=models.DateTimeField(auto_now_add=True)
    body=models.TextField()