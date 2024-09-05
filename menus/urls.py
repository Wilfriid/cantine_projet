from django.urls import path

from.views import menu ,menu_form


app_name = 'menus'

urlpatterns = [
    path('', menu, name='index'),
    path('menu_form/', menu_form, name='add'),
   

]