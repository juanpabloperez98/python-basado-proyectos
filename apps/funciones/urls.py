from django.urls import path
from . import views

app_name = 'funciones_app'


urlpatterns = [
    path('funciones',views.funciones.as_view(),name = 'funciones'),
    path('funcion',views.funcion.as_view(),name = 'funcion'),
    path('funciondef',views.funciondef.as_view(),name = 'funciondef'),
]