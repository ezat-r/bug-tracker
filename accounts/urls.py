from django.conf.urls import url, include
from .views import *
from . import password_reset_urls

# URLs specific to the 'accounts' app

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', registration, name="registration"),
    url(r'^password-reset/', include(password_reset_urls)),
]