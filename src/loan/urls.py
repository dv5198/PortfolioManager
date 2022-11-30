from django.urls import path

from .views import (
    add_loan,
    loan_details,
)

app_name = 'loans'

urlpatterns = [
    path('', loan_details, name='loan_detail'),
    path('check/', add_loan, name='check_loan'),
    path('add_loan/', add_loan, name='add_loan'),
]