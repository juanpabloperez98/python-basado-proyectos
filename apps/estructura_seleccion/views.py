from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class estructuras_seleccion(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/estructuras_seleccion.html"

class cif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/cif.html"

class condicionif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionif.html"

class ifejemplo1(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo1.html"

class ifejemplo2(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo2.html"

class ifejemplo3(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo3.html"

class ifejemplo4(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo4.html"

class ifejemplo5(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo5.html"

class ifejemplo6(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/cif/ejemplosif/ejemplo6.html"

class celif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/celif.html"

class condicionelif(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionelif.html"

class elifejemplo1(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo1.html"

class elifejemplo2(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo2.html"

class elifejemplo3(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo3.html"

class elifejemplo4(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo4.html"

class elifejemplo5(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo5.html"

class elifejemplo6(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celif/ejemploselif/ejemplo6.html"

class celse(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/celse.html"

class condicionelse(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/condiciones/condicionelse.html"
    
class elseejemplo1(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo1.html"

class elseejemplo2(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo2.html"

class elseejemplo3(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo3.html"

class elseejemplo4(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo4.html"

class elseejemplo5(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo51.html"

class elseejemplo6(TemplateView):
    template_name = "teoria/moduls/estructuras_seleccion/celse/ejemploselse/ejemplo6.html"