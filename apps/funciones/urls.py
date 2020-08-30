from django.urls import path
from . import views

app_name = 'funciones_app'


urlpatterns = [
    path('funciones',views.funciones.as_view(),name = 'funciones'),
    path('funcion',views.funcion.as_view(),name = 'funcion'),
    path('funciondef',views.funciondef.as_view(),name = 'funciondef'),
    path('ejemplo1',views.ejemplo1.as_view(),name = 'ejemplo1'),
    path('ejemplo2',views.ejemplo2.as_view(),name = 'ejemplo2'),
    path('ejemplo3',views.ejemplo3.as_view(),name = 'ejemplo3'),
    path('ejemplo4',views.ejemplo4.as_view(),name = 'ejemplo4'),
    path('ejemplo5',views.ejemplo5.as_view(),name = 'ejemplo5'),
    path('ejemplo6',views.ejemplo6.as_view(),name = 'ejemplo6'),
]