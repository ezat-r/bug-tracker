from django.conf.urls import url, include
from .views import *

# URLs specific to the 'bugDB' app

urlpatterns = [
    url(r'^all/$', bugsView, name="all_issues"),
    url(r'^create/$', createTicket, name="create_issue"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
]