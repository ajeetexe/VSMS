from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import Carousel, ServiceRequest, UserProfile
from django import forms
import datetime


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['vehicle_owner_name','vehicle_type','vehicle_name','vehicle_number','license_number','type_of_service','owner_address','appointment_date']
        widgets = {
            'appointment_date':widgets.DateInput(attrs={'type':'date'})
        }


class UserForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class UserForm2(forms.ModelForm):
    # dob = forms.DateField()

    # def clean_dob(self):
    #     dob = self.changed_data['dob']
    #     if dob > datetime.date.today():
    #         raise forms.ValidationError('')
    #     return dob
    class Meta:
        model = UserProfile
        fields = ['profile_pic','background_pic','dob','phone','gender','address',]
        widgets = {
            'dob':widgets.DateInput(attrs={'type':'date'}),
            'profile_pic':widgets.FileInput(),
            'background_pic':widgets.FileInput(),
        }


class CarouserForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['image','title','subtitle']