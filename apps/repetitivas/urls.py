from django.urls import path
from . import views

app_name = 'repetitivas_app'


urlpatterns = [
    path('estructuras-repetitivas',views.repetitivas.as_view(),name = 'repetitivas'),
    path('ciclosfor',views.ciclofor.as_view(),name = 'ciclofor'),
    path('indice',views.indice.as_view(),name = 'indice'),
    path('iterables',views.iterables.as_view(),name = 'iterables'),
    path('for-ejemplo1',views.ejemplo1.as_view(),name = 'for-ejemplo1'),
    path('for-ejemplo2',views.ejemplo2.as_view(),name = 'for-ejemplo2'),
    path('for-ejemplo3',views.ejemplo3.as_view(),name = 'for-ejemplo3'),
    path('for-ejemplo4',views.ejemplo4.as_view(),name = 'for-ejemplo4'),
    path('for-ejemplo5',views.ejemplo5.as_view(),name = 'for-ejemplo5'),
    path('for-ejemplo6',views.ejemplo6.as_view(),name = 'for-ejemplo6'),
    path('cicloswhile',views.ciclowhile.as_view(),name = 'ciclowhile'),
    path('conteo',views.conteo.as_view(),name = 'conteo'),
    path('otras-formas-while',views.otrasformas.as_view(),name = 'otrasformas'),
    path('while-ejemplo1',views.wejemplo1.as_view(),name = 'while-ejemplo1'),
    path('while-ejemplo2',views.wejemplo2.as_view(),name = 'while-ejemplo2'),
    path('while-ejemplo3',views.wejemplo3.as_view(),name = 'while-ejemplo3'),
    path('while-ejemplo4',views.wejemplo4.as_view(),name = 'while-ejemplo4'),
    path('while-ejemplo5',views.wejemplo5.as_view(),name = 'while-ejemplo5'),
    path('while-ejemplo6',views.wejemplo6.as_view(),name = 'while-ejemplo6'),

]