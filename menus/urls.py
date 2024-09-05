from django.urls import path
from.views import menu ,menu_form ,edit_menu , delete_menu


app_name = 'menus'

urlpatterns = [
    path('', menu, name='index'),
    path('menu_form/', menu_form, name='add'),
    path('edit_menu/<int:id>/', edit_menu, name='edit'),
    path('delete_menu/<int:id>/', delete_menu, name='delete'),
   

]