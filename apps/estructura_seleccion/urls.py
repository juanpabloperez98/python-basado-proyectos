from django.urls import path
from . import views

app_name = 'estructuras_seleccion_app'


urlpatterns = [
    path('estructuras-seleccion',views.estructuras_seleccion.as_view(),name = 'estructuras_seleccion'),
    path('cif',views.cif.as_view(),name = 'cif'),
    path('condicionif',views.condicionif.as_view(),name = 'condicionif'),
    path('if-ejemplo1',views.ifejemplo1.as_view(),name = 'if-ejemplo1'),
    path('if-ejemplo2',views.ifejemplo2.as_view(),name = 'if-ejemplo2'),
    path('if-ejemplo3',views.ifejemplo3.as_view(),name = 'if-ejemplo3'),
    path('if-ejemplo4',views.ifejemplo4.as_view(),name = 'if-ejemplo4'),
    path('if-ejemplo5',views.ifejemplo5.as_view(),name = 'if-ejemplo5'),
    path('if-ejemplo6',views.ifejemplo6.as_view(),name = 'if-ejemplo6'),
    path('celif',views.celif.as_view(),name = 'celif'),
    path('condicionelif',views.condicionelif.as_view(),name = 'condicionelif'),
    path('elif-ejemplo1',views.elifejemplo1.as_view(),name = 'elif-ejemplo1'),
    path('elif-ejemplo2',views.elifejemplo2.as_view(),name = 'elif-ejemplo2'),
    path('elif-ejemplo3',views.elifejemplo3.as_view(),name = 'elif-ejemplo3'),
    path('elif-ejemplo4',views.elifejemplo4.as_view(),name = 'elif-ejemplo4'),
    path('elif-ejemplo5',views.elifejemplo5.as_view(),name = 'elif-ejemplo5'),
    path('elif-ejemplo6',views.elifejemplo6.as_view(),name = 'elif-ejemplo6'),
    path('celse',views.celse.as_view(),name = 'celse'),
    path('condicionelse',views.condicionelse.as_view(),name = 'condicionelse'),
    path('else-ejemplo1',views.elseejemplo1.as_view(),name = 'else-ejemplo1'),
    path('else-ejemplo2',views.elseejemplo1.as_view(),name = 'else-ejemplo2'),
    path('else-ejemplo3',views.elseejemplo3.as_view(),name = 'else-ejemplo3'),
    path('else-ejemplo4',views.elseejemplo4.as_view(),name = 'else-ejemplo4'),
    path('else-ejemplo5',views.elseejemplo5.as_view(),name = 'else-ejemplo5'),
    path('else-ejemplo6',views.elseejemplo6.as_view(),name = 'else-ejemplo6'),
]