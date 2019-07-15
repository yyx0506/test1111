from django import forms
from .models import Artical,Myuser,Tag
from comment.models import Comment

class FormArtical(forms.ModelForm):
    class Meta:
        model=Artical
        ass = Tag.objects.all()
        ACTIVITY_STYLE = []
        for i in ass:
            a = (i.id, i.title)
            ACTIVITY_STYLE.append(a)
        AC = tuple(ACTIVITY_STYLE)
        fields = ["title", "body","category"]
        widgets = {
            "title": forms.TextInput(attrs={ "placeholder": "输入文章标题", "class": "form-control"}),
            # "body": forms.Textarea(
            #     attrs={"placeholder": "输入文本内容", "class": "form-control"}),

            "category":forms.Select(attrs={"class": "form-control"}),
        }
        tag=forms.MultipleChoiceField(label='标签云',choices=AC, widget=forms.CheckboxSelectMultiple())
        labels = {"title": "文章标题",
                  "body": "文本内容",
                  "category":"选择类型"
                  }


class FormComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ["body", "author", "email", "url"]


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, required=True, widget=forms.TextInput(
        attrs={"id": "username", "class": "form-control", "placeholder": "输入用户名"}))
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "id": "password", "placeholder": "输入密码", }))


class RegistForm(forms.ModelForm):
    repeatpassword = forms.CharField(label="重复密码",required=True,widget=forms.PasswordInput(attrs={"class":"form-control","id":"registpassword2", "placeholder":"输入确认密码"}))
    class Meta:
        model = Myuser
        fields = ["username","password","telephone",]
        widgets = {
            "username":forms.TextInput(attrs={"id":"registusername","placeholder": "输入账号","class":"form-control"}),
            "password": forms.PasswordInput(attrs={"id": "registpassword", "placeholder": "输入密码", "class":"form-control"}),
            "telephone": forms.TextInput(attrs={"id": "registphone", "placeholder": "输入手机号", "class": "form-control"})}
        help_texts={'username':''}
        labels={"username":"账户","password":"密码","telephone":"手机号"}
        password2=forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control", "id": "password2", "placeholder": "请再次输入密码", }))


