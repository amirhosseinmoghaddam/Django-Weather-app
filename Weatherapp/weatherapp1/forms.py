from django.forms import ModelForm
from .models import Locations

class CityForm(ModelForm):
    class Meta:
        model = Locations
        fields = ["location"]