from django.template import library
register =library.Library()
from goods.models import Goodsinfo,TypeInfo
from sellfresh.models import Cart


#自定义模板标签
@register.simple_tag
def getlatetype():
    return TypeInfo.objects.all()
@register.simple_tag
def getgoodsinfo(type,num=4):
    goods=Goodsinfo.objects.filter(goodstype=type).order_by('-id')[:num]
    return goods

@register.simple_tag
def getcartcount(person):
    Num=Cart.objects.filter(author=person).count
    return Num


