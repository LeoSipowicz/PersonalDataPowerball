from django import forms
from .models import PersonalDataModel
from .helper import Duplicates


POLITICAL_PARTY_CHOICES = [('rep', 'Republican'),
                           ('dem', 'Democrat'), ('ind', 'Independent')]
CONSENT_CHOICES = [('I agree', 'I agree')]
consentString = "I am over 18 years of age and consent to having my data shared freely with the winner of the personal data powerball"
emailConsentString = "I want to be contacted about future projects"
# Input form for personal data uses the db model for the personal data table


class PersonalDataForm(forms.ModelForm):
    political_party = forms.ChoiceField(
        choices=POLITICAL_PARTY_CHOICES,
        widget=forms.RadioSelect())
    consent = forms.ChoiceField(
        choices=CONSENT_CHOICES,
        label=consentString,
        widget=forms.RadioSelect())
    emailListConsent = forms.BooleanField(
        label=emailConsentString,
        initial=True)

    class Meta:
        model = PersonalDataModel
        fields = [
            "first_name",
            "last_name",
            "zipcode",
            "email",
            "phone",
            "political_party",
            "consent",
            "emailListConsent"]
        labels = {
            'first_name': 'First name',
            "last_name": 'Last name',
            "zipcode": 'Zipcode',
            "email": 'Email',
            "phone": 'Phone',
            "political_party": 'Political Party',
            "consent": consentString,
            "emailListConsent": emailConsentString,
            }
    def __init__(self, *args, **kwargs):
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        self.fields['emailListConsent'].required = False

# Input form form for picking balls
# Normal balls must be ints between 1 and 69
# Powerball must be int between 1 and 26
# No duplicates of normal balls are allowed


class PowerBallPickForm(forms.Form):
    ball1 = forms.IntegerField(label="Ball 1", max_value=69, min_value=1)
    ball2 = forms.IntegerField(label="Ball 2", max_value=69, min_value=1)
    ball3 = forms.IntegerField(label="Ball 3", max_value=69, min_value=1)
    ball4 = forms.IntegerField(label="Ball 4", max_value=69, min_value=1)
    ball5 = forms.IntegerField(label="Ball 5", max_value=69, min_value=1)
    powerBall = forms.IntegerField(label="Powerball", max_value=26, min_value=1)

    def clean(self):
        cleaned_data = super(PowerBallPickForm, self).clean()

        ballList = [
            cleaned_data.get("ball1"),
            cleaned_data.get("ball2"),
            cleaned_data.get("ball3"),
            cleaned_data.get("ball4"),
            cleaned_data.get("ball5")]
        dups = Duplicates(ballList)

        for x in dups:
            msg = "No duplicate balls please"
            self.add_error(x, msg)
