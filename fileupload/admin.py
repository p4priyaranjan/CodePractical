from django.contrib import admin
from .models import UserFile,UserEmail

# Register your models here.

@admin.register(UserFile)
class AdminUserFile(admin.ModelAdmin):
    list_display=['user','my_file']
