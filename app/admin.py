from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Carousel, UserProfile, ServiceRequest
# Register your models here.

admin.site.register(Carousel)
admin.site.register(ServiceRequest)
admin.site.register(UserProfile,ModelAdmin)