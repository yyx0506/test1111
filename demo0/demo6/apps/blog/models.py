from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.
class Myuser(User):
    telephone=models.IntegerField(default=110)
    type=models.IntegerField(default=0)

class Ads(models.Model):
    img=models.ImageField(upload_to="ads")
    title=models.CharField(max_length=20)
    index=models.IntegerField()
    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Tag(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Artical(models.Model):
    title=models.CharField(max_length=20)
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)
    view=models.IntegerField(default=0)
    author=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    body=UEditorField(imagePath="articalimg/",width="100%")
    # def __str__(self):
    #     return self.author,self.tag
