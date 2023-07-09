from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class UserRegistrationForm(UserCreationForm):
    #required=True/False, it's True by default

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']


# class BioForm(forms.ModelForm)


class EditUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','portfolio']
        labels = {'profile_pic':'Profile picture'}