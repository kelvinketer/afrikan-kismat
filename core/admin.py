from django.contrib import admin
from .models import SafariPackage, Destination, Inquiry, Testimonial, ItineraryDay, Partner

# --- 1. ITINERARY BUILDER (INLINE) ---
class ItineraryDayInline(admin.StackedInline):
    model = ItineraryDay
    extra = 0
    ordering = ('day_number',)

# --- 2. SAFARI PACKAGE ADMIN ---
@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    # CORRECTED FIELDS based on your model:
    # Used 'price_guideline' instead of 'price'
    # Used 'is_popular' instead of 'is_featured'
    list_display = ('title', 'location', 'duration_text', 'price_guideline', 'is_popular', 'is_luxury')
    
    search_fields = ('title', 'location')
    
    list_filter = ('is_popular', 'is_luxury', 'location')
    
    # These toggles are great for quick edits
    list_editable = ('is_popular', 'is_luxury')
    
    save_on_top = True
    inlines = [ItineraryDayInline]

# --- 3. DESTINATION ADMIN ---
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    # REMOVED 'country' to fix the error
    list_display = ('name', 'subtitle')
    
    search_fields = ('name', 'subtitle')

# --- 4. INQUIRY ADMIN ---
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

# --- 5. TESTIMONIAL ADMIN ---
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # Used 'client_name' based on your previous code
    list_display = ('client_name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')
    list_editable = ('is_active',)

# --- 6. PARTNER ADMIN ---
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'order')
    list_editable = ('order',)
    ordering = ('order',)