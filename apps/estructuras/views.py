from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class estructuras(TemplateView):
    template_name = "teoria/moduls/estructuras/estructuras_datos.html"

