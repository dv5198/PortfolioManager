import json
from django.http import JsonResponse
import requests

def stock_data_NIFTY_50(request):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

    main_url = "https://www.nseindia.com/"
    response = requests.get(main_url, headers=headers)
    # print(response.status_code)
    cookies = response.cookies

    preopen_market_url = "https://www.nseindia.com/api/market-data-pre-open?key=NIFTY"
    preopen_data = requests.get(
        preopen_market_url, headers=headers, cookies=cookies)
    # print(preopen_data.status_code)
    # print("Pre-open market data", preopen_data.json())

    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    nifty_50_data = requests.get(url, headers=headers, cookies=cookies)
    # print(nifty_50_data.status_code)
    nifty50_data = nifty_50_data.json()
    # print(nifty50_data)

    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20BANK"
    nifty_bank_data = requests.get(url, headers=headers, cookies=cookies)
    # print(nifty_bank_data.status_code)
    nifty_bank_data = nifty_bank_data.json()
    return JsonResponse(nifty50_data)


def stock_data_NIFTY_BANK(request):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

    main_url = "https://www.nseindia.com/"
    response = requests.get(main_url, headers=headers)
    print(response.status_code)
    cookies = response.cookies

    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20BANK"
    nifty_bank_data = requests.get(url, headers=headers, cookies=cookies)
    # print(nifty_bank_data.status_code)
    nifty_bank_data = nifty_bank_data.json()
    return JsonResponse(nifty_bank_data)

def stock_data_SENSEX(request):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    url = "https://api.bseindia.com/RealTimeBseIndiaAPI/api/GetSensexData/w?code=16"
    sensex_data = requests.get(url,headers=headers)
    
    sensex_data=sensex_data.json()
    print(sensex_data)
    return JsonResponse(sensex_data,safe=False)
