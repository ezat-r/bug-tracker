from django.conf.urls import url, include
from .views import *
from . import password_reset_urls

# URLs specific to the 'bugDB' app

urlpatterns = [
    url('login/', login, name="login"),
    url(r'^$', allIssuesView, name="all_issues"),
    url(r'^create/$', createTicket, name="create_issue"),
    url(r'^view-issue/(?P<id>[0-9]+)/$', issueDetailedView, name="detailed_view"),
    url(r'^edit-issue/(?P<id>[0-9]+)/$', editIssue, name="edit_issue"),
    url(r'^resolve-issue/(?P<id>[0-9]+)/$', resolveIssue, name="resolve_issue"),
    url(r'^close-issue/(?P<id>[0-9]+)/$', closeIssue, name="resolve_issue"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', registration, name="registration"),
    url(r'^password-reset/', include(password_reset_urls)),
]