from django.contrib import admin
from .models import *
import xadmin
class ArticalAdmin:
    style_fields={"body": "ueditor"}
# Register your models here.
xadmin.site.register(Artical,ArticalAdmin)
xadmin.site.register(Myuser)
xadmin.site.register(Ads)
xadmin.site.register(Category)
xadmin.site.register(Tag)
