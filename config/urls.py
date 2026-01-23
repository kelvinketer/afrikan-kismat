from django.contrib import admin
from django.urls import path, include  # <--- Added 'include' here
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
    
    # Safari Detail Page
    path('safari/<int:pk>/', views.safari_detail, name='safari_detail'),

    # PAYMENTS APP (This is the new line connecting M-Pesa)
    path('payments/', include('payments.urls')),
    
    path('blog/', include('blog.urls')),
]