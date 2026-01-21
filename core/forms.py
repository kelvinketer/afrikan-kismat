from django import forms
from .models import Inquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'subject', 'message']
        
        # We can style the inputs using Tailwind classes here
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded p-3 focus:outline-none focus:border-safari-clay',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded p-3 focus:outline-none focus:border-safari-clay',
                'placeholder': 'name@example.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded p-3 focus:outline-none focus:border-safari-clay',
                'placeholder': 'Safari Interest / General Question'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-gray-50 border border-gray-200 rounded p-3 focus:outline-none focus:border-safari-clay h-32',
                'placeholder': 'Tell us about your dream trip...'
            }),
        }