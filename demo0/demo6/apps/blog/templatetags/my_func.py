from django.template import library
register =library.Library()
from blog.models import Artical,Category,Tag
#自定义模板标签
@register.simple_tag
def getlatestaticles(num=3):
    return Artical.objects.order_by("-createtime")[:num]
@register.simple_tag
#分类
def getallcategray():
    return Category.objects.all()
@register.simple_tag
#标签云
def getalltag():
    return Tag.objects.all()
@register.simple_tag
#时间归档通过月份进行去重
def gettimes():
    times= Artical.objects.dates("createtime","month")
    print(times)
    return times
#自定义过滤器 不建议使用
@register.filter
def myupper(value):
    return value.capitalize()
