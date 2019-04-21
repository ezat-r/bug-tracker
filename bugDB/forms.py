from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    #Form to be used to login users

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

