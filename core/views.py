from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# --- UPDATED IMPORT: Added 'Partner' to the list ---
from .models import SafariPackage, Destination, Testimonial, Partner
from .forms import ContactForm

# --- VIEWS ---

def home(request):
    # 1. Fetch active testimonials (Top 3)
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-id')[:3]
    
    # 2. Fetch Destinations for the Slider
    # We exclude the "Big 3" popular ones because they are already hardcoded 
    # in the "Popular Destinations" grid on the homepage.
    slider_destinations = Destination.objects.exclude(
        slug__in=['masai-mara', 'amboseli', 'diani-beach']
    )
    
    # Fallback: If the database is empty or has few items, just grab all of them 
    # to prevent an empty slider.
    if not slider_destinations.exists():
        slider_destinations = Destination.objects.all()

    # 3. Fetch Featured Safaris (First 3)
    safari_packages = SafariPackage.objects.all().order_by('-id')[:3]

    # 4. NEW: Fetch Partners for the scrolling logos
    # We grab all partners to display in the footer/slider area
    partners = Partner.objects.all()

    context = {
        'testimonials': testimonials,
        'slider_destinations': slider_destinations,
        'safari_packages': safari_packages,
        'partners': partners, # <--- Pass the partners to the template
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # 1. If user hit "Submit", process the data
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # 2. Save the data to the "Inquiry" database table
            form.save()
            
            # 3. Show a success message (The "Asante!" popup)
            messages.success(request, "Asante! We have received your message and will contact you shortly.")
            
            # 4. Reload the page to clear the form
            return redirect('contact')
    else:
        # 5. If user just visited the page (GET request)
        
        # --- SMART PRE-FILL LOGIC ---
        # Check if the URL has a 'package' parameter (e.g. ?package=Mara+Adventure)
        package_name = request.GET.get('package', '')
        
        initial_data = {}
        if package_name:
            initial_data = {
                'subject': f"Inquiry regarding: {package_name}",
                'message': f"Hi, I am interested in booking the {package_name}. Please send me more details."
            }
        
        # Pass 'initial' data to the form to pre-fill the fields automatically
        form = ContactForm(initial=initial_data)
        # --- END SMART PRE-FILL ---

    return render(request, 'contact.html', {'form': form})

def safaris(request):
    # Fetch all safari packages from the database
    all_safaris = SafariPackage.objects.all()
    return render(request, 'safaris.html', {'safaris': all_safaris})

def destinations(request):
    # Fetch all destinations for the catalog page
    all_destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def destination_detail(request, slug):
    # Fetch the specific destination from the database by its slug
    destination = get_object_or_404(Destination, slug=slug)
    
    return render(request, 'destination_detail.html', {'destination': destination})

def safari_detail(request, pk):
    # Fetch the specific safari by its primary key (ID)
    safari = get_object_or_404(SafariPackage, pk=pk)
    
    # Suggest similar safaris (exclude the current one) to keep users browsing
    related_safaris = SafariPackage.objects.exclude(pk=pk)[:3]
    
    context = {
        'safari': safari,
        'related_safaris': related_safaris
    }
    
    return render(request, 'safari_detail.html', context)