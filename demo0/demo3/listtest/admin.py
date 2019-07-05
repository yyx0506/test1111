from django.contrib import admin
from .models import *
# Register your models here.
class Choiceinline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","pub_date")
    list_filter = ("question_text","pub_date")
    # list_per_page = 1
    inlines = [Choiceinline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text","votes","question")
    list_filter = ("choice_text","votes")
    #list_per_page = 1

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
