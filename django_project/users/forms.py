from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inherits usercreationform
    email = forms.EmailField()

    class Meta: #gives nested namespace and keeps them i one place
        model = User #affecsts the user model
        fields = ['username', 'email', 'password1', 'password2'] #these are the fields we want and in this order

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']