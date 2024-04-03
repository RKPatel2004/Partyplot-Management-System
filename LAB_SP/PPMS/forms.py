from .models import Admin
from django import forms
from .models import Venue


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'location', 'capacity', 'amenities', 'pricing', 'availability', 'image']


