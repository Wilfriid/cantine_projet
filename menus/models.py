# menus/models.py
from django.db import models

class Menu(models.Model):
    plat = models.OneToOneField('plats.Plat', on_delete=models.CASCADE)  # Référence correcte
    date_creation = models.DateTimeField(auto_now_add=True)

    

