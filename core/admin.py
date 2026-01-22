from django.contrib import admin
from .models import SafariPackage, Destination, Testimonial, ItineraryDay, Inquiry, Partner

# Inline editing for Itinerary Days inside the Safari Package page
class ItineraryDayInline(admin.TabularInline):
    model = ItineraryDay
    extra = 1

@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_text', 'price_guideline', 'is_popular', 'is_luxury')
    search_fields = ('title', 'location')
    list_filter = ('is_popular', 'is_luxury')
    inlines = [ItineraryDayInline]

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    # FIXED: Replaced 'subject' with 'package' and added smart fields
    list_display = ('name', 'package', 'phone', 'travel_date', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message', 'phone')
    readonly_fields = ('created_at',)
    list_editable = ('is_processed',) # Allows you to check/uncheck "Handled" from the list

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'is_active')
    list_filter = ('is_active', 'rating')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'order')
    list_editable = ('order',)