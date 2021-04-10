from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Carousel, UserProfile
# Register your models here.

admin.site.register(Carousel)
admin.site.register(UserProfile,ModelAdmin)