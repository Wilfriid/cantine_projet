from django.urls import path

from.views import plat , plat_form


app_name = 'plat'

urlpatterns = [
    path('', plat, name='index'),
    path('plat_form/', plat_form, name='add'),
    
   

]