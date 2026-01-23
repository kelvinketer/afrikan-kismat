from decimal import Decimal # <--- Added this import
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.models import SafariPackage
from .models import Transaction
from .mpesa_utils import MpesaClient

# CONFIGURABLE EXCHANGE RATE (Now safely converted to Decimal)
USD_TO_KES_RATE = Decimal('132.00') 

# --- 1. THE SIMPLE TEST PAGE VIEW ---
def initiate_payment(request):
    if request.method == 'GET':
        return render(request, 'pay_test.html')

    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount', '1')
        
        if not phone:
            messages.error(request, "Please enter a phone number.")
            return redirect('test_payment')

        client = MpesaClient()
        try:
            response = client.stk_push(phone, amount)
            if response.get('ResponseCode') == '0':
                messages.success(request, f"STK Push Sent! Check your phone ({phone}).")
            else:
                messages.error(request, f"M-Pesa Error: {response.get('errorMessage')}")
        except Exception as e:
            messages.error(request, f"System Error: {str(e)}")
            
        return redirect('test_payment')


# --- 2. THE REAL SAFARI BOOKING VIEW ---
def initiate_safari_payment(request, safari_id):
    safari = get_object_or_404(SafariPackage, pk=safari_id)
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        
        # Default to 1 traveler if not specified
        try:
            travelers = int(request.POST.get('travelers', 1))
        except ValueError:
            travelers = 1
        
        if not phone:
            messages.error(request, "Phone number is required.")
            return redirect('safari_detail', pk=safari_id)

        # 1. Calculate Costs
        # Now both are Decimals, so Python is happy!
        total_usd = safari.price_usd * travelers
        total_kes = int(total_usd * USD_TO_KES_RATE)

        # 2. Save "Pending" Transaction
        transaction = Transaction.objects.create(
            safari=safari,
            phone_number=phone,
            amount_usd=total_usd,
            exchange_rate=USD_TO_KES_RATE,
            amount_kes=total_kes,
            status="PENDING"
        )

        # 3. Trigger M-Pesa
        client = MpesaClient()
        try:
            response = client.stk_push(phone, total_kes, account_reference="Safari Booking")
            
            if response.get('ResponseCode') == '0':
                transaction.mpesa_request_id = response.get('CheckoutRequestID')
                transaction.save()
                messages.success(request, f"Request sent! Please check your phone ({phone}) to pay KES {total_kes}.")
            else:
                transaction.status = "FAILED"
                transaction.save()
                messages.error(request, f"M-Pesa Error: {response.get('errorMessage')}")
                
        except Exception as e:
            transaction.status = "ERROR"
            transaction.save()
            messages.error(request, f"System Error: {str(e)}")

        return redirect('safari_detail', pk=safari_id)

    return redirect('safari_detail', pk=safari_id)

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

# ... keep your existing imports and views ...

# --- 3. THE PAYMENT SUCCESS LOGIC ---
def handle_successful_payment(transaction):
    """
    This function performs all the 'After Payment' actions:
    1. Marks DB as Success
    2. Sends Receipt Email
    """
    # 1. Update Database
    transaction.status = "SUCCESS"
    transaction.save()

    # 2. Prepare Email Content
    subject = f"Booking Confirmed: {transaction.safari.title}"
    
    # We create a simple text receipt
    message = f"""
    Jambo! 
    
    We have received your payment of KES {transaction.amount_kes}.
    
    RECEIPT DETAILS:
    ----------------
    Transaction ID: {transaction.mpesa_request_id or 'N/A'}
    Safari: {transaction.safari.title}
    Travelers: {int(transaction.amount_usd / transaction.safari.price_usd)}
    Date Paid: {timezone.now().strftime('%Y-%m-%d %H:%M')}
    
    YOUR ITINERARY:
    ---------------
    You can view your full itinerary on our website here:
    http://127.0.0.1:8000/safari/{transaction.safari.id}/
    
    Karibu Safari!
    The Afrikan Kismat Team
    """
    
    # 3. Send Email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL], # sending to admin for test (since we didn't ask for user email in form)
        fail_silently=False,
    )
    
    # --- 4. DEV TOOL: SIMULATE SUCCESS ---
def debug_simulate_success(request, transaction_id):
    """
    DEV ONLY: Forces a transaction to be successful so we can test emails.
    """
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    handle_successful_payment(transaction)
    messages.success(request, "Simulation: Payment marked as SUCCESS. Receipt email sent!")
    return redirect('safari_detail', pk=transaction.safari.id)