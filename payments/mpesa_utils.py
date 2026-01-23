import requests
import json
import base64
from datetime import datetime
from django.conf import settings

class MpesaClient:
    def __init__(self):
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET
        self.api_url = "https://sandbox.safaricom.co.ke"  # Use 'api.safaricom.co.ke' for Live
        
    def get_access_token(self):
        """authenticate with Safaricom and get a temporary token"""
        url = f"{self.api_url}/oauth/v1/generate?grant_type=client_credentials"
        response = requests.get(url, auth=(self.consumer_key, self.consumer_secret))
        
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception("Failed to get Access Token")

    def stk_push(self, phone_number, amount, account_reference="Afrikan Kismat"):
        """Trigger the popup on the user's phone"""
        token = self.get_access_token()
        headers = {"Authorization": f"Bearer {token}"}
        
        # timestamp format: YYYYMMDDHHmmss
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        
        # password = base64(shortcode + passkey + timestamp)
        shortcode = settings.MPESA_SHORTCODE
        passkey = settings.MPESA_PASSKEY
        password_str = f"{shortcode}{passkey}{timestamp}"
        password = base64.b64encode(password_str.encode()).decode()

        payload = {
            "BusinessShortCode": shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),
            "PartyA": phone_number,  # The phone sending money
            "PartyB": shortcode,     # The business receiving
            "PhoneNumber": phone_number,
            "CallBackURL": "https://your-app-name.onrender.com/payments/callback/", # We will build this later
            "AccountReference": account_reference,
            "TransactionDesc": "Safari Payment"
        }
        
        url = f"{self.api_url}/mpesa/stkpush/v1/processrequest"
        response = requests.post(url, json=payload, headers=headers)
        
        return response.json()