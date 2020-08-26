from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class funciones(TemplateView):
    template_name = "teoria/moduls/funciones/funciones.html"

class funcion(TemplateView):
    template_name = "teoria/moduls/funciones/funcion/funcion.html"

class funciondef(TemplateView):
    template_name = "teoria/moduls/funciones/func/funciondef.html"