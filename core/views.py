from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import SafariPackage, Destination, Testimonial, Partner
from .forms import InquiryForm  # <--- Updated Import (was ContactForm)

# --- VIEWS ---

def home(request):
    # 1. Fetch active testimonials (Top 3)
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-id')[:3]
    
    # 2. Fetch Destinations for the Slider
    slider_destinations = Destination.objects.exclude(
        slug__in=['masai-mara', 'amboseli', 'diani-beach']
    )
    
    if not slider_destinations.exists():
        slider_destinations = Destination.objects.all()

    # 3. Fetch Featured Safaris (First 3)
    safari_packages = SafariPackage.objects.all().order_by('-id')[:3]

    # 4. Fetch Partners
    partners = Partner.objects.all()

    context = {
        'testimonials': testimonials,
        'slider_destinations': slider_destinations,
        'safari_packages': safari_packages,
        'partners': partners,
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # 1. If user hit "Submit", process the data
        form = InquiryForm(request.POST)
        
        if form.is_valid():
            # 2. Save the data
            form.save()
            
            # 3. Show a success message
            messages.success(request, "Asante! We have received your message and will contact you shortly.")
            
            # 4. Reload
            return redirect('contact')
    else:
        # 5. Generic Empty Form
        form = InquiryForm()

    return render(request, 'contact.html', {'form': form})

def safaris(request):
    all_safaris = SafariPackage.objects.all()
    return render(request, 'safaris.html', {'safaris': all_safaris})

def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    return render(request, 'destination_detail.html', {'destination': destination})

def safari_detail(request, pk):
    # Fetch the specific safari
    safari = get_object_or_404(SafariPackage, pk=pk)
    
    # --- SMART INQUIRY LOGIC START ---
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Save the inquiry but pause to add the package link
            inquiry = form.save(commit=False)
            inquiry.package = safari  # Link this inquiry to THIS specific safari
            inquiry.save()
            
            messages.success(request, "Asante! We have received your quote request. Our team will contact you shortly.")
            return redirect('safari_detail', pk=pk)
    else:
        # Pre-fill the form slightly? No, keep it clean for now.
        form = InquiryForm()
    # --- SMART INQUIRY LOGIC END ---

    # Suggest similar safaris
    related_safaris = SafariPackage.objects.exclude(pk=pk)[:3]
    
    context = {
        'safari': safari,
        'related_safaris': related_safaris,
        'form': form, # <--- Pass the form to the template
    }
    
    return render(request, 'safari_detail.html', context)