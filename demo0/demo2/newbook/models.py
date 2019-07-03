from django.db import models

# Create your models here.
class Newbook(models.Model):
    title=models.CharField(max_length=20)
    datetime=models.DateTimeField(auto_now=True)
class Newhero(models.Model):
    name=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    book = models.ForeignKey(Newbook, on_delete=models.CASCADE)
