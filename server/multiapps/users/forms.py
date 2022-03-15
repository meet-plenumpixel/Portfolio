from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from users.models import ProfileModel

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#   email = forms.EmailField()

#   class Meta:
#     model = User
#     fields = ['username', 'email']


# class UserProfileUpdateForm(forms.ModelForm):

#   class Meta:
#     model = ProfileModel
#     fields = ['image']
