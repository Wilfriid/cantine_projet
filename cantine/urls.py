
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ma_cantine/',include("ma_cantine.urls")),
    path('menus/',include("menus.urls")),
    path('plats/',include("plats.urls")),
]
