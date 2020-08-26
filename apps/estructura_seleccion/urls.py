from django.urls import path
from . import views

app_name = 'estructuras_seleccion_app'


urlpatterns = [
    path('estructuras-seleccion',views.estructuras_seleccion.as_view(),name = 'estructuras_seleccion'),
    path('cif',views.cif.as_view(),name = 'cif'),
    path('celif',views.celif.as_view(),name = 'celif'),
    path('celse',views.celse.as_view(),name = 'celse'),
    path('condicionif',views.condicionif.as_view(),name = 'condicionif'),
    path('condicionelif',views.condicionelif.as_view(),name = 'condicionelif'),
    path('condicionelse',views.condicionelse.as_view(),name = 'condicionelse'),
]