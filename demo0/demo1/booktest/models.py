from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateTimeField(auto_now=True)


class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=5,choices=(("man","男"),("woman","女")))
    # gender=models.BooleanField(default=True)
    content=models.CharField(max_length=100)
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)