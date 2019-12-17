from django.contrib.auth.models import User
from django import forms
from .models import UserProfileInfo

class signUpForm(forms.ModelForm):

    class Meta:
        model=UserProfileInfo
        fields=['profile_pic','phonenumber','bio','birth_date']

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField(max_length=255,help_text='Valid email required')

    class Meta():
        model=User
        fields=('username','password','email','first_name','last_name')
