from django.contrib import admin
from django.db import models
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

class UserAdminForm(UserAdmin):
    ordering=['-email']
    list_display=['email','user_name','first_name','last_name']
    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','phone_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser','login_attempts_left', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number','email','user_name','password1', 'password2','is_active','is_staff'),
        }),
    )
admin.site.register(CustomUser,UserAdminForm)

# @admin.register(CustomUser,UserAdminConfig)
# class AdminUser(admin.ModelAdmin):
#     pass