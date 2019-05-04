from django import forms
from .models import Payment

class MakeCardPaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2025)]

    credit_card_number = forms.CharField(label="Card Number", required=False)
    cvv = forms.CharField(label="CVV", required=False)
    expiry_month = forms.ChoiceField(label="Expiry Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class UserPaymentDetailsForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ("fullName", "streetAddress1", "streetAddress2", "country", "postCode")
        labels = {
            "fullName": "Full Name",
            "streetAddress1": "Street Address 1",
            "streetAddress2": "Street Address 2",
            "postCode": "Post Code",
        }

        