from django.shortcuts import render, redirect
from django.contrib import messages
from .mpesa_utils import MpesaClient

def initiate_payment(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount', '1') # Default to 1 KES for testing
        
        if not phone:
            messages.error(request, "Please enter a phone number.")
            return redirect('safaris') # Redirect back if error

        client = MpesaClient()
        
        try:
            # Call the engine
            response = client.stk_push(phone, amount)
            
            if response.get('ResponseCode') == '0':
                messages.success(request, f"STK Push Sent! Check your phone ({phone}).")
            else:
                error_message = response.get('errorMessage', 'Payment failed.')
                messages.error(request, f"M-Pesa Error: {error_message}")
                
        except Exception as e:
            messages.error(request, f"System Error: {str(e)}")
            
        return redirect('safaris') # Stay on page to show message

    return redirect('home')