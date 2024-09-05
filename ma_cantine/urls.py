from django.urls import path

from.views import ma_cantine


app_name = 'ma_cantine'

urlpatterns = [
    path('', ma_cantine, name='index'),
   

]