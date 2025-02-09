from django import forms
from .models import AstronomicalObject

class AstronomicalObjectForm(forms.ModelForm):
    class Meta:
        model = AstronomicalObject
        fields = '__all__'
