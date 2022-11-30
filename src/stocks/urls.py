from django.urls import path

from .views import (
    stock_data_NIFTY_50,
    stock_data_NIFTY_BANK,
    stock_data_SENSEX
)

app_name = 'stocks'

urlpatterns = [
    path('', stock_data_NIFTY_50, name='stock_details'),
    path('nifty_bank/', stock_data_NIFTY_BANK, name='stock_details_niftybank'),
    path('sensex/', stock_data_SENSEX, name='stock_details_sensex'),
    
]