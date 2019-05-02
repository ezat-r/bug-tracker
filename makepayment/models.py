from django.db import models
from bugDB.models import Issue

class Payment(models.Model):
    fullName = models.CharField(max_length=50, blank=False)
    streetAddress1 = models.CharField(max_length=40, blank=False)
    streetAddress2 = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postCode = models.CharField(max_length=20, blank=False)
    paymentDate = models.DateTimeField()

    issue = models.ForeignKey(Issue, null=False)
