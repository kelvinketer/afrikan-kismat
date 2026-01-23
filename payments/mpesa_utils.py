import requests
import json
import base64
from datetime import datetime
from django.conf import settings

class MpesaClient:
    def __init__(self):
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET
        self.api_url = "https://sandbox.safaricom.co.ke"
        
    def get_access_token(self):
        url = f"{self.api_url}/oauth/v1/generate?grant_type=client_credentials"
        response = requests.get(url, auth=(self.consumer_key, self.consumer_secret))
        
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception("Failed to get Access Token")

    def format_phone_number(self, phone):
        """
        Cleans and formats phone number to 2547XXXXXXXX
        """
        # 1. Remove all spaces and + signs
        phone = str(phone).strip().replace(" ", "").replace("+", "")
        
        # 2. If it starts with '0', replace with '254'
        if phone.startswith("0"):
            phone = "254" + phone[1:]
            
        # 3. Ensure it is exactly 12 digits
        if len(phone) != 12 or not phone.isdigit():
            raise ValueError("Invalid phone number format. Use 07XXXXXXXX")
            
        return phone

    def stk_push(self, phone_number, amount, account_reference="Afrikan Kismat"):
        try:
            # Clean the phone number first
            clean_phone = self.format_phone_number(phone_number)
            
            token = self.get_access_token()
            headers = {"Authorization": f"Bearer {token}"}
            
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
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
                "PartyA": clean_phone,
                "PartyB": shortcode,
                "PhoneNumber": clean_phone,
                "CallBackURL": "https://kismatexpeditions.com/payments/callback/",
                "AccountReference": account_reference,
                "TransactionDesc": "Safari Payment"
            }
            
            url = f"{self.api_url}/mpesa/stkpush/v1/processrequest"
            response = requests.post(url, json=payload, headers=headers)
            
            return response.json()
            
        except ValueError as e:
            # Return our own error if the number format was bad
            return {'ResponseCode': '400', 'errorMessage': str(e)}
        except Exception as e:
            return {'ResponseCode': '500', 'errorMessage': str(e)}