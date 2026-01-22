from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        # We now include the new smart fields: phone, travel_date, adults, children
        fields = ['name', 'email', 'phone', 'travel_date', 'adults', 'children', 'message']
        
        # Tailwind Styling for all inputs
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition',
                'placeholder': 'name@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition',
                'placeholder': 'WhatsApp / Phone Number'
            }),
            'travel_date': forms.DateInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition text-gray-500',
                'type': 'date'  # This triggers the browser's date picker
            }),
            'adults': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition',
                'min': '1',
                'value': '2'
            }),
            'children': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay transition',
                'min': '0',
                'value': '0'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded-lg px-4 py-3 focus:outline-none focus:border-safari-clay h-32 transition',
                'placeholder': 'Tell us about your dream trip (special diet, interests, etc.)...'
            }),
        }