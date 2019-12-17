from django.contrib.auth.models import User
from django.contrib,auth.models import UserCreationForm
from django import forms
from .models import UserProfileInfo

class signUpForm(UserCreationForm):
    email=forms.EmailField(max_length=255,help_text='Valid email required')

    class Meta:
        model=UserProfileInfo
        fields=['username','email','password1','password2','first_name','last_name','profile_pic','phonenumber','bio','birth_date']
