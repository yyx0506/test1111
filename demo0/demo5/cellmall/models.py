from django.db import models

# Create your models here.

class LoginManage(models.Manager):
    def iflogin(self, _name, _password):
        aa=User.objects.get(name=_name,password=_password)
        if aa:
            aa.type=1
            aa.save()
            tips="登陆成功"
        else:
            tips="登陆失败"
        return tips
    def ifregest(self,_name,_password,_password2):
        if _password!=_password2:
            tips="两次输入密码不一致"
        else:
            User.objects.all()
            if User.objects.filter(username=_name):
                tips = "账号已注册"
            else:
                uu=User(username=_name,password=_password)
                uu.save()
                tips = "注册成功"
            return tips
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=11)
    type=models.IntegerField(max_length=11,default=0)
    objects=LoginManage()
class Userinfo(models.Model):
    usernickname=models.CharField(max_length=20)
    usertelephone=models.IntegerField(max_length=20)
    uu=models.OneToOneField(User,on_delete=models.CASCADE)
    objects = LoginManage()

