from django.contrib import admin
from .models import *
# Register your models here.
#
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date', 'author', 'image')

admin.site.register(News)
admin.site.register(Region)
admin.site.register(Category)
