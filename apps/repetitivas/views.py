from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class repetitivas(TemplateView):
    template_name = "teoria/moduls/repetitivas/repetitivas.html"


class ciclofor(TemplateView):
    template_name = "teoria/moduls/repetitivas/ciclos_for.html"


class indice(TemplateView):
    template_name = "teoria/moduls/repetitivas/porindice/indice.html"


class iterables(TemplateView):
    template_name = "teoria/moduls/repetitivas/iterables/iterables.html"


class ejemplo1(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo1.html"


class ejemplo2(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo2.html"


class ejemplo3(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo3.html"


class ejemplo4(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo4.html"


class ejemplo5(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo5.html"


class ejemplo6(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemplosfor/ejemplo6.html"

class ciclowhile(TemplateView):
    template_name = "teoria/moduls/repetitivas/ciclos_while.html"

class conteo(TemplateView):
    template_name = "teoria/moduls/repetitivas/por_conteo/conteo.html"
    
class otrasformas(TemplateView):
    template_name = "teoria/moduls/repetitivas/otras_formas/formas.html"


class wejemplo1(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo1.html"

class wejemplo2(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo2.html"

class wejemplo3(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo3.html"

class wejemplo4(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo4.html"

class wejemplo5(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo5.html"

class wejemplo6(TemplateView):
    template_name = "teoria/moduls/repetitivas/ejemploswhile/ejemplo6.html"
