from django.urls import path
from . import views

app_name = 'proyecto1_app'

urlpatterns = [
    path('proyecto1',views.proyecto1.as_view(),name = 'proyecto1'),
    path('proyecto1/parte1',views.parte1.as_view(),name = 'proyecto1-part1'),
    path('proyecto1/parte2',views.parte2.as_view(),name = 'proyecto1-part2'),
    path('proyecto1/parte3',views.parte3.as_view(),name = 'proyecto1-part3'),
    path('proyecto1/parte4',views.parte4.as_view(),name = 'proyecto1-part4'),
    path('proyecto1/parte5',views.parte5.as_view(),name = 'proyecto1-part5'),
    path('proyecto1/parte6',views.parte6.as_view(),name = 'proyecto1-part6'),
    path('proyecto1/parte7',views.parte7.as_view(),name = 'proyecto1-part7'),
    path('proyecto1/final',views.final.as_view(),name = 'proyecto1-final'),
]