from django.shortcuts import render, redirect
from menus.forms import MenuForm
from menus.models import Menu

# Create your views here.


def menu(request):
    menus = Menu.objects.all()
    return render(request, 'pages/menus.html', {'menus': menus})


def menu_form(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menus:index')  
    else:
        form = MenuForm()
    
    return render(request, 'pages/menu_forms.html', {'form': form})




