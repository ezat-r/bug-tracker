from django.conf.urls import url
from .views import *

# URLs specific to the 'search' app

urlpatterns = [
    url(r'^$', search, name="search"),
]