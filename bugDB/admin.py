from django.contrib import admin
from .models import Issue, IssueComments

# Register your models here.

admin.site.register(Issue)

admin.site.register(IssueComments)
