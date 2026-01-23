from django.urls import path
from . import views

urlpatterns = [
    # 1. Simple M-Pesa Test Page
    path('test-pay/', views.initiate_payment, name='test_payment'),
    
    # 2. Real Safari Booking Logic
    path('book/<int:safari_id>/', views.initiate_safari_payment, name='book_safari'),
    
    # 3. Development Tool: Simulate Success (For Receipts)
    path('simulate-success/<int:transaction_id>/', views.debug_simulate_success, name='simulate_success'),
]