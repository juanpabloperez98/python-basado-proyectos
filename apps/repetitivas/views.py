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