# menus/forms.py
from django import forms
from .models import Menu
from plats.models import Plat  

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['plat']  
        
    plat = forms.ModelChoiceField(queryset=Plat.objects.all())


