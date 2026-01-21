from django.contrib import admin
from django.urls import path
from core import views  # Ensure views is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('safaris/', views.safaris, name='safaris'),
    
    # NEW: Add this line
    path('destinations/', views.destinations, name='destinations'), 
    
    path('destination/<slug:slug>/', views.destination_detail, name='destination_detail'),
]