from django import forms
from .models import City, Flight

# форма добавления городов
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'region', 'latitude', 'longitude']


# для рейсов
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            'airline',
            'origin',
            'destination',
            'departure_time',
            'arrival_time',
            'status',
            'seats_available',
            'class_type'
        ]
