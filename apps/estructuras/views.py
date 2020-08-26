from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class estructuras(TemplateView):
    template_name = "teoria/moduls/estructuras/estructuras_datos.html"


class cadenas(TemplateView):
    template_name = "teoria/moduls/estructuras/cadenas.html"


class operaciones(TemplateView):
    template_name = "teoria/moduls/estructuras/operaciones.html"


class formateo(TemplateView):
    template_name = "teoria/moduls/estructuras/formateo.html"


class ejemplo1(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo1.html"


class ejemplo2(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo2.html"


class ejemplo3(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo3.html"


class ejemplo4(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo4.html"


class ejemplo5(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo5.html"


class ejemplo6(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos/ejemplo6.html"


class listas(TemplateView):
    template_name = "teoria/moduls/estructuras/listas.html"


class manejolistas(TemplateView):
    template_name = "teoria/moduls/estructuras/manejolistas.html"


class operacioneslistas(TemplateView):
    template_name = "teoria/moduls/estructuras/operacioneslistas.html"


class lejemplo1(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo1.html"


class lejemplo2(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo2.html"


class lejemplo3(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo3.html"


class lejemplo4(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo4.html"


class lejemplo5(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo5.html"


class lejemplo6(TemplateView):
    template_name = "teoria/moduls/estructuras/ejemplos_listas/ejemplo6.html"
