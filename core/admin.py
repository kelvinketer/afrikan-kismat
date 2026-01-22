from django.contrib import admin
from .models import SafariPackage, Destination, Inquiry, Testimonial, ItineraryDay, Partner

# --- 1. ITINERARY BUILDER (INLINE) ---
# Allows adding "Day 1", "Day 2" directly inside the Safari Page
class ItineraryDayInline(admin.StackedInline):
    model = ItineraryDay
    extra = 0  # Changed to 0 so it doesn't clutter the screen if not needed
    ordering = ('day_number',)

# --- 2. SAFARI PACKAGE ADMIN ---
@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    # Columns to show in the list
    list_display = ('title', 'location', 'duration_text', 'price_guideline', 'is_popular', 'is_luxury')
    
    # Add a Search Bar for these fields
    search_fields = ('title', 'location', 'overview')
    
    # Filter sidebar (Right side)
    list_filter = ('is_popular', 'is_luxury', 'location')
    
    # Editable toggles directly in the list view (Huge time saver!)
    list_editable = ('is_popular', 'is_luxury')
    
    # Save button at the top and bottom
    save_on_top = True
    
    # Register the Itinerary Builder here
    inlines = [ItineraryDayInline]

# --- 3. DESTINATION ADMIN ---
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    # Auto-generate the URL slug from the name
    prepopulated_fields = {'slug': ('name',)}
    
    list_display = ('name', 'country', 'subtitle')
    search_fields = ('name', 'country')
    list_filter = ('country',)

# --- 4. INQUIRY ADMIN (MESSAGES) ---
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    
    # Show newest messages first
    ordering = ('-created_at',)

# --- 5. TESTIMONIAL ADMIN ---
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')
    list_editable = ('is_active',)  # Quickly publish/unpublish reviews

# --- 6. PARTNER ADMIN ---
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'order')
    list_editable = ('order',)  # Quickly re-arrange logo order
    ordering = ('order',)