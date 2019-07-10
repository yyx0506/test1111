from django import forms
from .models import MyUser
# class form(forms.ModelForm):
# class  Loginform(forms.Form):
#     username=forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={}))
#     password=forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={}))
#     from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, required=True, widget=forms.TextInput(
        attrs={"id": "username", "class": "form-control", "placeholder": "输入用户名"}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "id": "password", "placeholder": "输入密码", }))
class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码",required=True,widget=forms.PasswordInput(attrs={"class":"form-control","id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = MyUser
        fields = ["username","password","telephone",]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder": "输入账号","class":"form-control"}),
            "password": forms.PasswordInput(attrs={"id": "registpassword", "placeholder": "输入密码", "class":"form-control"}),
            "telephone": forms.TextInput(attrs={"id": "registphone", "placeholder": "输入手机号", "class": "form-control"})}
        help_texts={'username':''}
        labels={"username":"账户","password":"密码","telephone":"手机号"}
        password2=forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "id": "password2", "placeholder": "请再次输入密码", }))
