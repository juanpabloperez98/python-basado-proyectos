from django.urls import path
from . import views

app_name = 'estructuras_app'


urlpatterns = [
    path('estructuras-datos',views.estructuras.as_view(),name = 'datos'),
]