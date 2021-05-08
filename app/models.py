from django import forms
from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/%y/%m/%d')
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user_name, filename)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name='Profile Picture',blank=True,null=True,upload_to=user_directory_path)
    dob = models.DateField(default=None, verbose_name='Date Of Birth')
    phone = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('m','Male'),('f','Female'),('o','Other')),blank=True, null=True)
    address = models.TextField()



    def __str__(self) -> str:
        return str(self.user)
