from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Issue

class UserLoginForm(forms.Form):
    #Form to be used to login users

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    # form used to register a new user

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

    # anything with 'clean_' will clean the relevant input elements
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique")

        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ("projectName", "issueType", "issuePriority", "issuePriority", "title", "affectsVersion", "foundInBuild", "description", "status", "reporter")
    

    