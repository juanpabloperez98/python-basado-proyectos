from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('apps.main.urls')),
    re_path('',include('apps.repetitivas.urls')),
    re_path('',include('apps.estructuras.urls')),
    re_path('',include('apps.graficos.urls')),
    re_path('',include('apps.proyecto1.urls')),
    re_path('',include('apps.proyecto2.urls')),
    re_path('',include('apps.proyecto3.urls')),
    re_path('',include('apps.funciones.urls')),
    re_path('',include('apps.estructura_seleccion.urls')),
]
