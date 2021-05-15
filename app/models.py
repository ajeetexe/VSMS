from django import forms
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import datetime

# Create your models here.
def carousel_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = datetime.datetime.now()
    return "Carousel/{0}.{1}".format(filename, ext)

class Carousel(models.Model):
    image = ProcessedImageField(
        upload_to=carousel_directory_path,
        processors=[ResizeToFill(1200, 600)],
        format="JPEG",
        options={"quality": 80},
    )
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = datetime.datetime.now()
    return "user/{0}/{1}.{2}".format(instance.user, filename, ext)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = ProcessedImageField(
        verbose_name="Profile Picture",
        upload_to=user_directory_path,
        default="default/profile.png",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 80},
    )
    background_pic = ProcessedImageField(
        verbose_name="Background Picture",
        upload_to=user_directory_path,
        default="default/bg_1.jpg",
        processors=[ResizeToFill(820, 312)],
        format="JPEG",
        options={"quality": 80},
    )
    dob = models.DateField(verbose_name="Date Of Birth", blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=(("m", "Male"), ("f", "Female"), ("o", "Other")),
        blank=True,
        null=True,
    )
    address = models.TextField()

    def __str__(self) -> str:
        return str(self.user)

    # def delete(self, using, keep_parents: bool):
    #     return super().delete(using=using, keep_parents=keep_parents)


class Mechanics(models.Model):
    full_name = models.CharField(verbose_name="Full Name", max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(
        max_length=10, choices=(("m", "Male"), ("f", "Female"), ("o", "Other"))
    )
    address = models.TextField()

    def __str__(self) -> str:
        return self.full_name


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_owner_name = models.CharField(max_length=150)
    service_request_no = models.CharField(
        max_length=30, primary_key=True, unique=True, editable=False
    )
    service_request_date = models.DateTimeField(auto_now_add=True)
    vehicle_type = models.CharField(
        max_length=1, choices=(("b", "Bike"), ("c", "Car"), ("s", "Scooter"))
    )
    vehicle_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    type_of_service = models.CharField(
        max_length=1, choices=(("s", "Service Centre"), ("h", "Home Service"))
    )
    owner_address = models.TextField()
    mechanics_name = models.ForeignKey(
        Mechanics, on_delete=models.CASCADE, blank=True, null=True
    )
    appointment_date = models.DateField(blank=True, null=True)
    service_charge = models.IntegerField(default=0)
    parts_charge = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10, choices=(("p", "Pending"), ("a", "Approve")), default="p"
    )

    def __str__(self) -> str:
        return f"User: {self.user} Request No.: {self.service_request_no}"

    @property
    def sum(self):
        return self.service_charge + self.parts_charge
