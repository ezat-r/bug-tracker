from django.conf.urls import url
from .views import *

# URLs specific to the 'makepayment' app

urlpatterns = [
    url(r'^(?P<id>[0-9]+)', enterPaymentInfo, name="make_payment"),
]