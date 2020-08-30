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

class ejemplo1(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/moduls/funciones/ejemplos/ejemplo6.html"