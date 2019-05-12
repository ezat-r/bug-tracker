from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.shortcuts import render
from django.conf import settings
from bugDB.models import Issue, IssueComments
from .models import Payment
from .forms import MakeCardPaymentForm, UserPaymentDetailsForm
from datetime import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET

def enterPaymentInfo(request, id):

    # check if user is already logged in
    if request.user.is_authenticated == False:
        # user is not logged in, so redirect to login page
        return redirect(reverse("login"))
    
    issue = get_object_or_404(Issue, id=id)

    # check if user has attempted a payment
    if request.method=="POST":
        # payment has been attempted
        userDetalsForm = UserPaymentDetailsForm(request.POST)
        cardDetailsForm = MakeCardPaymentForm(request.POST)
        
        # check if both forms are valid
        if userDetalsForm.is_valid() and cardDetailsForm.is_valid():
            
            # forms are valid, so attempt a payment of £10 using Stripe API
            try:
                makePayment = stripe.Charge.create(
                    amount = 1000,
                    currency = "GBP",
                    description = request.user.email,
                    card = cardDetailsForm.cleaned_data['stripe_id'],
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if makePayment.paid:
                # if payment has been paid successfully, then go ahead and save the payment details to DB
                order = userDetalsForm.save(commit=False)
                order.paymentDate = datetime.now()
                order.issue = issue
                order.save()
                
                # increment the issue 'votes' property by 1 & save it to DB
                issue.votes += 1
                issue.updatedDate = datetime.now()
                issue.save()

                # Display a success message & re-direct back to the issue page
                messages.success(request, "You have successfully paid")

                return redirect("detailed_view", id=id)
            
            else:
                # otherwise, display a error message & re-direct to issue page
                messages.error(request, "Unable to take payment")

                return redirect("detailed_view", id=id)
        else:

            # Display error message and re-direct to issue page
            messages.error(request, "We were unable to take a payment with that card!")

            return redirect("detailed_view", id=id)
            
    else:
        # otherwise, send empty forms to view
        userDetalsForm = UserPaymentDetailsForm()
        cardDetailsForm = MakeCardPaymentForm()

    viewObjects = {"issue": issue, "userDetailsForm": userDetalsForm, "cardDetailsForm": cardDetailsForm, "publishable": settings.STRIPE_PUBLISHABLE}

    return render(request, "make-payment/make-payment.html", viewObjects)