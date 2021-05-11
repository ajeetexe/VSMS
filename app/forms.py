from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import ServiceRequest, UserProfile
from django import forms


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
    class Meta:
        model = UserProfile
        fields = ['profile_pic','background_pic','dob','phone','gender','address']