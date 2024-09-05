from django.shortcuts import get_object_or_404, render, redirect
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

def edit_menu(request, id):
    menu = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menus:index')
    else:
        form = MenuForm(instance=menu)
    
    return render(request, 'pages/edit_menu.html', {'form': form, 'menu': menu})


def delete_menu(request, id):
    menu = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        menu.delete()
        return redirect('menus:index')
    return render(request, 'pages/delete_menu.html', {'menu': menu})






