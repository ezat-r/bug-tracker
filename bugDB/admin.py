from django.contrib import admin
from .models import Issue, IssueComments, IssueProject

# Register your models here.

admin.site.register(IssueProject)

admin.site.register(Issue)

admin.site.register(IssueComments)
