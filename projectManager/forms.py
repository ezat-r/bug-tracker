from django import forms
from django.forms import ModelForm
from .models import IssueProject

class IssueProjectForm(ModelForm):

    class Meta:
        model = IssueProject
        fields = ["projectName"]
