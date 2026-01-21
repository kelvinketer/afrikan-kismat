from django.contrib import admin
from .models import SafariPackage, Destination, Inquiry, Testimonial, ItineraryDay

# --- 1. ITINERARY BUILDER (INLINE) ---
# This allows you to add "Day 1", "Day 2", etc. directly inside the Safari Page
class ItineraryDayInline(admin.StackedInline):
    model = ItineraryDay
    extra = 1  # Display one empty form by default
    ordering = ('day_number',)

# --- 2. MAIN MODELS ---

@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'duration_text', 'price_guideline', 'is_popular', 'is_luxury')
    search_fields = ('title', 'location')
    list_filter = ('is_popular', 'is_luxury')
    
    # Register the Inline here
    inlines = [ItineraryDayInline]

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} 
    list_display = ('name', 'subtitle')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',) 

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')