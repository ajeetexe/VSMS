from io import SEEK_END
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, ServiceRequest


@receiver(post_save,sender=User)
def create_user(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# @receiver(pre_save,sender=User)
# def change_user(sender, instance, **kwargs):
#     if instance.username:
#         try:
#             old_profile_pic = UserProfile.objects.get(user = instance).profile_pic
#         except UserProfile.DoesNotExist:
#             return
#         else:
#             new_profile_pic = instance.userprofile.profile_pic
#             if old_profile_pic and old_profile_pic.url != new_profile_pic.url:
#                 old_profile_pic.delete(save=False)