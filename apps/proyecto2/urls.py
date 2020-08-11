from django.urls import path
from . import views

app_name = 'proyecto2_app'

urlpatterns = [
    path('proyecto2',views.proyecto2.as_view(),name = 'proyecto2'),
    path('proyecto2/parte1',views.part1.as_view(),name = 'part1'),
    path('proyecto2/parte2',views.part2.as_view(),name = 'part2'),
    path('proyecto2/parte3',views.part3.as_view(),name = 'part3'),
    path('proyecto2/parte4',views.part4.as_view(),name = 'part4'),
    path('proyecto2/parte5',views.part5.as_view(),name = 'part5'),
    path('proyecto2/parte6',views.part6.as_view(),name = 'part6'),
    path('proyecto2/parte7',views.part7.as_view(),name = 'part7'),
    path('proyecto2/parte8',views.part8.as_view(),name = 'part8'),
    path('proyecto2/parte9',views.part9.as_view(),name = 'part9'),
    path('proyecto2/parte10',views.part10.as_view(),name = 'part10'),
    path('proyecto2/parte11',views.part11.as_view(),name = 'part11'),
    path('proyecto2/final',views.final.as_view(),name = 'proyecto2-final'),
]