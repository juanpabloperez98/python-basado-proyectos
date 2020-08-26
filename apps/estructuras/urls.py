from django.urls import path
from . import views

app_name = 'estructuras_app'


urlpatterns = [
    path('estructuras-datos',views.estructuras.as_view(),name = 'datos'),
    path('cadenas-caracteres',views.cadenas.as_view(),name = 'cadenas-caracteres'),
    path('cadenas-caracteres/operaciones',views.operaciones.as_view(),name = 'operaciones'),
    path('cadenas-caracteres/formateo',views.formateo.as_view(),name = 'formateo'),
    path('cadenas-caracteres/ejemplo1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('cadenas-caracteres/ejemplo2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('cadenas-caracteres/ejemplo3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('cadenas-caracteres/ejemplo4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('cadenas-caracteres/ejemplo5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('cadenas-caracteres/ejemplo6',views.ejemplo6.as_view(),name = 'ejemplo6'),
    path('listas',views.listas.as_view(),name = 'listas'),
    path('listas/manejo-listas',views.manejolistas.as_view(),name = 'manejo-listas'),
    path('listas/operaciones',views.operacioneslistas.as_view(),name = 'operaciones-listas'),
    path('listas/ejemplo1',views.lejemplo1.as_view(),name = 'lejemplo1'),
    path('listas/ejemplo2',views.lejemplo2.as_view(),name = 'lejemplo2'),
    path('listas/ejemplo3',views.lejemplo3.as_view(),name = 'lejemplo3'),
    path('listas/ejemplo4',views.lejemplo4.as_view(),name = 'lejemplo4'),
    path('listas/ejemplo5',views.lejemplo5.as_view(),name = 'lejemplo5'),
    path('listas/ejemplo6',views.lejemplo6.as_view(),name = 'lejemplo6'),

]