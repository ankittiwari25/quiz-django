from django.contrib import admin
from .models import *
# Register your models here.

class User(admin.ModelAdmin):
    fields = ['name','email']
    search_fields = ['name']
    list_filter = ['name','email']
    list_display = ['name','email']

class Question(admin.ModelAdmin):
    fields = ['question','answer',' catagory']
    search_fields = ['catagory']
    list_filter = ['question']
    list_display = ['question','answer']

class Java(admin.ModelAdmin):
    fields = ['question','answer']
    search_fields = ['question']
    list_filter = ['question']
    list_display = ['question','answer']

class CC(admin.ModelAdmin):
    fields = ['question','answer']
    search_fields = ['question']
    list_filter = ['question']
    list_display = ['question','answer']

class Python(admin.ModelAdmin):
    fields = ['question','answer']
    search_fields = ['question']
    list_filter = ['question']
    list_display = ['question','answer']

class Android(admin.ModelAdmin):
    fields = ['question','answer',' catagory']
    search_fields = ['question']
    list_filter = ['question']
    list_display = ['question','answer']


admin.site.site_header = 'Quiz Administration'
admin.site.register(Register,User)
admin.site.register(Questions,Question)
admin.site.register(Advancejava,Java)
admin.site.register(C,CC)
admin.site.register(Advancepython,Python)
admin.site.register(Advanceandroid,Android)
admin.site.register(Result)
