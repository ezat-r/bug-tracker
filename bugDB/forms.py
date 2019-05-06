from django import forms
from django.forms import ModelForm
from .models import Issue, IssueComments

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["issueProjectName", "issueType", "title", "affectsVersion", "foundInBuild", "description"]

class IssueCommentsForm(ModelForm):
    class Meta:
        model = IssueComments
        fields = ["comment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["comment"].widget.attrs.update({"class": "materialize-textarea", "placeholder": "Enter comment..."})
    

    