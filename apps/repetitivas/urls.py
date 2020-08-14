from django.urls import path
from . import views

app_name = 'repetitivas_app'


urlpatterns = [
    path('/estructuras-repetitivas',views.repetitivas.as_view(),name = 'repetitivas'),
    path('/ciclosfor',views.ciclofor.as_view(),name = 'ciclofor'),
    path('/indice',views.indice.as_view(),name = 'indice'),
    path('/iterables',views.iterables.as_view(),name = 'iterables'),
    
]