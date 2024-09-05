from django.urls import path
from.views import plat , plat_form ,edit_plat,delete_plat


app_name = 'plat'

urlpatterns = [
    path('', plat, name='index'),
    path('plat_form/', plat_form, name='add'),
    path('edit_plat/<int:id>/', edit_plat, name='edit'),
    path('delete_plat/<int:id>/',delete_plat, name='delete'),
]

    
    
   

