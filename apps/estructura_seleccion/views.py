from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class estructuras_seleccion(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/estructuras_seleccion.html"

class cif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/cif.html"

class celif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/celif.html"

class celse(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/celse.html"

class condicionif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionif.html"

class condicionelif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionelif.html"

class condicionelse(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionelse.html"