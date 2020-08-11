from django.urls import path
from . import views

app_name = 'graficos_app'

urlpatterns = [
    path('graficos/',views.home.as_view(),name = 'graficos-index'),
    path('tkinter/',views.tkinter.as_view(),name = 'graficos-tkinter'),
    # Primera interfaz grafica
    path('primera-interfaz/',views.firts_gui.as_view(),name = 'graficos-firts-gui'),
    # Interfaz Grafica con Frames
    path('frames/',views.frames.as_view(),name = 'graficos-frames'),
    # Interfaz grafica con Labels
    path('labels/',views.labels.as_view(),name = 'graficos-labels'),

]