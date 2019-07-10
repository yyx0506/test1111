from django.contrib import admin
from .models import *
import xadmin
# Register your models here.
xadmin.site.register(Artical)
xadmin.site.register(Myuser)
xadmin.site.register(Ads)
xadmin.site.register(Category)
xadmin.site.register(Tag)
