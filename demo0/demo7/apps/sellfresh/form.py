from django import forms
from .models import Myuser,Address,Comment

class FormAddress(forms.ModelForm):
    class Meta:
        model=Address
        fields = ["person", "address", "zip", "telephone"]

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, required=True, widget=forms.TextInput(
        attrs={"id": "username", "class": "name_input", "placeholder": "输入用户名"}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={"class": "pass_input", "id": "password", "placeholder": "输入密码", }))

class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="确认密码",required=True,widget=forms.PasswordInput(attrs={"id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = Myuser
        fields = ["username","password","telephone","email"]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder": "输入账号"}),
            "password": forms.PasswordInput(attrs={"id": "registpassword", "placeholder": "输入密码"}),
            "telephone": forms.TextInput(attrs={"id": "registphone", "placeholder": "输入手机号"}),
            "email":forms.EmailInput(attrs={"id":"email","placeholder": "输入邮箱"})}
        help_texts={'username':''}
        # labels={"username":"用户名","password":"密码","telephone":"手机号"}

class FormComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ["comment"]