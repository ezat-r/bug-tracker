from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.shortcuts import render
from bugDB.models import Issue, IssueComments
from .models import Payment
from .forms import MakeCardPaymentForm, UserPaymentDetailsForm
from datetime import datetime

def enterPaymentInfo(request, id):
    issue = get_object_or_404(Issue, id=id)
    userDetalsForm = UserPaymentDetailsForm()
    cardDetailsForm = MakeCardPaymentForm()

    viewObjects = {"issue": issue, "userDetailsForm": userDetalsForm, "cardDetailsForm": cardDetailsForm}

    return render(request, "make-payment/make-payment.html", viewObjects)