from django.contrib import admin
from .models import *
# Register your models here.
# class Goodinfoinline(admin.StackedInline):
#     model = Goodsinfo
#     extra = 1
class TypeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    # list_per_page = 1
    # inlines = [Goodinfoinline]
class GoodsinfoAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    # list_per_page = 1
admin.site.register(Goodsinfo,GoodsinfoAdmin)
admin.site.register(TypeInfo,TypeAdmin)