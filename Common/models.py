from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,user_name,first_name,last_name,password,phone_number,**other_fields):
        if not email:
            raise ValueError(_('You Must Provide An Email Address'))
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,last_name=last_name,phone_number=phone_number,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,first_name,user_name,last_name,password,phone_number,**other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned with is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned with is_superuser=True')

        return self.create_user(email,user_name,first_name,last_name,password,phone_number,**other_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_('email address'),max_length=40,blank=False,unique=True)
    user_name=models.CharField(max_length=20,blank=False,unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    phone_number=models.BigIntegerField(blank=False,unique=True)
    login_attempts_left=models.PositiveIntegerField(default=3)

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=['user_name','first_name','last_name','email']
    objects=CustomUserManager()

    def __str__(self):
        return self.user_name
