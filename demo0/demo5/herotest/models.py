from django.db import models

# Create your models here.


class AddManage(models.Manager):
    def addhero(self,_name,_content,_book,_gender):
        hero=Hero()
        hero.name = _name
        hero.content = _content
        hero.book = _book
        hero.gender = _gender
        hero.save()
    def addbook(self,_name):
        book=Book()
        book.name=_name
        book.save()
class Book(models.Model):
    name=models.CharField(max_length=50)
    pub_datime=models.DateTimeField(auto_now=True)
    objects = AddManage()
class Hero(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(choices=(("man","男"),("woman","女")),max_length=20,default="man")
    content=models.CharField(max_length=20)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    objects = AddManage()