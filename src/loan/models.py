import uuid
from django.db import models

from users.models import User

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

MARRIED_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

EDUCATION_CHOICES = [
    ('Graduate', 'Graduate'),
    ('Not Graduate', 'Not Graduate'),
]

SELF_EMPLOYED_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

PROPERTY_AREA_CHOICES = [
    ('Urban', 'Urban'),
    ('Semiurban', 'Semiurban'),
    ('Rural', 'Rural'),
]

# Create your models here.
class Loan(models.Model):

    loan_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=30,choices=GENDER_CHOICES)
    married = models.CharField(max_length=30,choices=MARRIED_CHOICES)
    dependents = models.CharField(max_length=30)
    education = models.CharField(max_length=30,choices=EDUCATION_CHOICES)
    self_employed = models.CharField(max_length=30,choices=SELF_EMPLOYED_CHOICES)
    applicant_income = models.PositiveIntegerField(max_length=30)
    coapplicant_income = models.PositiveIntegerField(max_length=30)
    loanAmount = models.PositiveIntegerField(max_length=30)
    loan_Amount_term = models.CharField(max_length=30)
    credit_history = models.CharField(max_length=30)
    property_area = models.CharField(max_length=30,choices=PROPERTY_AREA_CHOICES)
    loan_status=models.CharField(max_length=20)
    
    def __str__(self):
        return self.user
    

