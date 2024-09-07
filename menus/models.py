# menus/models.py
from django.db import models

class Menu(models.Model):
    plat = models.OneToOneField('plats.Plat', on_delete=models.CASCADE)  
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Menu du {self.plat}'    

