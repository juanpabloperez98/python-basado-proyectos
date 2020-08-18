from django.urls import path
from . import views

app_name = 'proyecto3_app'
urlpatterns = [
    path('proyecto3',views.proyecto3.as_view(),name = 'proyecto3'),
    path('proyecto3/parte1',views.part1.as_view(),name = 'part1'),
    path('proyecto3/parte2',views.part2.as_view(),name = 'part2'),
    path('proyecto3/parte3',views.part3.as_view(),name = 'part3'),
    path('proyecto3/parte4',views.part4.as_view(),name = 'part4'),

]