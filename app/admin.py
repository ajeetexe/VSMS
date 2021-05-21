from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Carousel, UserProfile, ServiceRequest, Mechanics
from django.contrib.auth.models import Group, User
# Register your models here.





admin.site.register(Carousel)
admin.site.register(ServiceRequest)
admin.site.register(UserProfile)
admin.site.register(Mechanics)
