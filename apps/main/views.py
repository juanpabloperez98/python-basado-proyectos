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


# Operadores
class operadores(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/operadores.html"

class tipos_operadores_asig(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_operadores/asignacion.html"

class tipos_operadores_arit(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_operadores/aritmeticos.html"

class tipos_operadores_rel(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/tipos_operadores/relacionales.html"

# Ejemplos Operadores
class ejemplo1_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo1.html"

class ejemplo2_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo2.html"

class ejemplo3_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo3.html"

class ejemplo4_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo4.html"

class ejemplo5_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo5.html"

class ejemplo6_op(TemplateView):
    template_name = "teoria/moduls/estructura_secuencia/ejemplos_operadores/ejemplo6.html"

class proyectos(TemplateView):
    template_name = "proyectos/index.html"
