from django.contrib import admin
from django.urls import path
from core import views  # Import views from your core app

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Core Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Main Listings
    path('safaris/', views.safaris, name='safaris'),
    path('destinations/', views.destinations, name='destinations'),
    
    # Detail Pages
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
    
    # NEW: The Safari Detail Page (using the Database ID 'pk')
    path('safari/<int:pk>/', views.safari_detail, name='safari_detail'),
]