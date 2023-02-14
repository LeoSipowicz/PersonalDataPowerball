from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class PersonalDataModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(region="CA")
    political_party = models.CharField(max_length=20)
    consent = models.CharField(max_length=7)
    emailListConsent = models.BooleanField()
    
