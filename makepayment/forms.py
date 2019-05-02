from django import forms
from .models import Payment

class MakeCardPaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2025)]
    TEST = ["Bish", "Bash", "Bosh"]

    credit_card_number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label='CVV', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    test = forms.ChoiceField(label='Test', choices=TEST, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class UserPaymentDetailsForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('fullName', 'streetAddress1', 'streetAddress2', 'country', 'postCode')