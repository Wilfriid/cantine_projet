# plats/views.py
from django.shortcuts import get_object_or_404, render, redirect
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

def edit_plat(request, id):
    plat = get_object_or_404(Plat, id=id)
    if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('plat:index')
    else:
        form = PlatForm(instance=plat)
    
    return render(request, 'pages/edit_plat.html', {'form': form, 'plat': plat})

# Suppression d'un menu
def delete_plat(request, id):
    plat = get_object_or_404(Plat, id=id)
    if request.method == 'POST':
        plat.delete()
        return redirect('plat:index')
    
    return render(request, 'pages/delete_plat.html', {'plat': plat})


