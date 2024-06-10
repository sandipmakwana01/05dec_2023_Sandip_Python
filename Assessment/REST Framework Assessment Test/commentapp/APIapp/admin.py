from django.contrib import admin
from .models import commentInfo

# Register your models here.

class commentdata(admin.ModelAdmin):
    list_display=['name','email','comment']

admin.site.register(commentInfo,commentdata)