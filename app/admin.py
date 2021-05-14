from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Carousel, UserProfile, ServiceRequest, Mechanics
from django.contrib.auth.models import Group, User
# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ("username","first_name", "last_name", "email","is_active","is_staff","last_login","date_joined")

     ## Static overriding 
    fieldsets = (
         (None, {'fields': ('username', 'password')}),
         (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
         (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups')}),
     (('Important dates'), {'fields': ('last_login', 'date_joined')}),
     )


class UserProfileAdmin(admin.ModelAdmin):

     def image_tag(self,obj):
          return obj.image_tag
     image_tag.allow_tags = True

admin.site.register(Carousel)
admin.site.register(ServiceRequest)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.unregister(Group)
admin.site.register(Mechanics)
