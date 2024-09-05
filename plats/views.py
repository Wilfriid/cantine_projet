# plats/views.py
from django.shortcuts import render, redirect
from plats.forms import PlatForm
from plats.models import Plat  # Importation correcte depuis models.py

def plat(request):
    plats = Plat.objects.all()
    return render(request, 'pages/plats.html', {'plats': plats})

def plat_form(request):
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plat:index')  
    else:
        form = PlatForm()
    return render(request, 'pages/plat_forms.html', {'form': form})


