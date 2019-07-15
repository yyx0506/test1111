from django.contrib import admin
from .models import *
# Register your models here.
class HeroInfoinline(admin.StackedInline):
    model = HeroInfo
    extra = 1
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ("title","pub_date")
    list_filter = ("title","pub_date")
    # list_per_page = 1
    inlines = [HeroInfoinline]
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ("name","content","gender","book")
    list_filter = ("name","content","gender")
    # list_per_page = 1

admin.site.register(Bookinfo,BookinfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
