from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# used to handle the password reset urls
urlpatterns = [
    url(r"^$", password_reset, name="password_reset"),
    url(r"^done/$", password_reset_done, name="password_reset_done"),
    url(r"^confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$", password_reset_confirm, name="password_reset_confirm"),
    url(r"^complete/$", password_reset_complete, name="password_reset_complete")
]