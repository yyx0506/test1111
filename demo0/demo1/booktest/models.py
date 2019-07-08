from django.db import models

class Ads(models.Model):
    title=models.CharField(max_length=20)
    img=models.ImageField(upload_to="static/img/")
    def __str__(self):
        return self.title

class HeroInfoManage(models.Manager):
    def addhero(self,_name,_content,_book,_gender):
        hero=HeroInfo()
        hero.name = _name
        hero.content = _content
        hero.book = _book
        hero.gender = _gender
        hero.save()
# Create your models here.
class Bookinfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=5,choices=(("man","男"),("woman","女")))
    # gender=models.BooleanField(default=True)
    content=models.CharField(max_length=100)
    book=models.ForeignKey(Bookinfo,on_delete=models.CASCADE)
    objects=HeroInfoManage()

#1对多
class User(models.Model):
    name=models.CharField(max_length=20)

class Account(models.Model):
    telephone=models.CharField(max_length=20)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
#1对1
class Onestep(models.Model):
    name=models.CharField(max_length=20)
class Telephone(models.Model):
    phone=models.CharField(max_length=20)
    name=models.OneToOneField(Onestep,on_delete=models.CASCADE)
#多对多
class Host(models.Model):
    host=models.CharField(max_length=20)
class Application(models.Model):
    app=models.CharField(max_length=20)
    name=models.ManyToManyField(Host)