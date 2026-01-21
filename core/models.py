from django.db import models

class SafariPackage(models.Model):
    # Basic Info
    title = models.CharField(max_length=200)  # e.g., "Mara Budget Adventure"
    duration_text = models.CharField(max_length=50, help_text="e.g. 3 Days / 2 Nights")
    location = models.CharField(max_length=100, help_text="e.g. Masai Mara")
    
    # Image (We will use URL for now to keep it simple with Unsplash)
    image_url = models.URLField(max_length=500, help_text="Paste the Unsplash image link here")
    
    # Details
    description = models.TextField()
    price_guideline = models.CharField(max_length=100, blank=True, help_text="e.g. From $400 pp")
    
    # Badges (Checkboxes in Admin)
    is_popular = models.BooleanField(default=False, verbose_name="Mark as Most Popular")
    is_luxury = models.BooleanField(default=False, verbose_name="Mark as Luxury")

    def __str__(self):
        return self.title
    

# ... (SafariPackage class is above this)

class Destination(models.Model):
    name = models.CharField(max_length=200)  # e.g., "Masai Mara"
    slug = models.SlugField(unique=True, help_text="URL text (e.g., 'masai-mara'). Must be unique.")
    subtitle = models.CharField(max_length=200) # e.g., "The World Cup of Wildlife"
    image_url = models.URLField(max_length=500)
    description = models.TextField()
    
    # Facts Sidebar
    best_time = models.CharField(max_length=100, help_text="e.g. July to October")
    ideal_stay = models.CharField(max_length=100, help_text="e.g. 3-4 Days")
    wildlife = models.CharField(max_length=200, help_text="e.g. Big 5, Cheetah, Hippo")
    
    # Highlights (We will store them as a simple list separated by commas)
    highlights = models.TextField(help_text="Enter highlights separated by commas (e.g., 'Big 5, Hot Air Balloon, Cultural Visits')")

    def __str__(self):
        return self.name

    # Helper to split highlights for the template
    def get_highlights_list(self):
        return [h.strip() for h in self.highlights.split(',')]
    
    # ... (Destination Model is above this)

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="General Inquiry")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    # ... (Inquiry model is above this)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100, default="Safari Traveler", help_text="e.g. 'Family from Texas' or 'Solo Traveler'")
    image_url = models.URLField(blank=True, help_text="Optional: Link to client photo")
    quote = models.TextField()
    rating = models.IntegerField(default=5, help_text="1 to 5 stars")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client_name} ({self.rating} stars)"
    

# ... existing imports (make sure SafariPackage is defined above this)

class ItineraryDay(models.Model):
    safari = models.ForeignKey(SafariPackage, related_name='itinerary_days', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(help_text="e.g. 1, 2, 3")
    title = models.CharField(max_length=200, help_text="e.g. Arrival in Nairobi")
    description = models.TextField()
    accommodation = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. Sarova Stanley Hotel")
    meals = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Breakfast, Lunch, Dinner")

    class Meta:
        ordering = ['day_number']
        verbose_name = "Itinerary Day"
        verbose_name_plural = "Itinerary Days"

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"