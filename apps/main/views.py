from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class home(TemplateView):
    template_name = "index.html"

class teoria_index(TemplateView):
    template_name = "teoria/index.html"

class estructuras_de_secuencia(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/estructurasecuencia.html"

class tipos_datos(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_datos.html"

class numeros(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_datos/numeros.html"

class secuencia(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_datos/secuencia.html"

# Ejemplos tipos de datos
class ejemplo1_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo1.html"

class ejemplo2_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo2.html"

class ejemplo3_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo3.html"

class ejemplo4_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo4.html"

class ejemplo5_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo5.html"

class ejemplo6_td(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_tipos_datos/ejemplo6.html"


