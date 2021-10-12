from django.db import models
from Common.models import CustomUser

# Create your models here.

class UserFile(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    my_file=models.FileField(upload_to='media/doc',blank=True)

class UserEmail(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email_sec=models.EmailField(max_length=100,blank=False)
