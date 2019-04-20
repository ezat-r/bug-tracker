from django.conf.urls import url, include
from .views import *

# URLs specific to the 'bugDB' app

urlpatterns = [
    url(r'^all-bugs/$', bugsView),
    url(r'^create/$', createTicket),
]