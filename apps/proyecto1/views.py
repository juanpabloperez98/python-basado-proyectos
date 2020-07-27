from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class proyecto1(TemplateView):
    template_name = "proyectos/proyecto1/index.html"

class parte1(TemplateView):
    template_name = "proyectos/proyecto1/part1.html"

class parte2(TemplateView):
    template_name = "proyectos/proyecto1/part2.html"

class parte3(TemplateView):
    template_name = "proyectos/proyecto1/part3.html"

class parte4(TemplateView):
    template_name = "proyectos/proyecto1/part4.html"

class parte5(TemplateView):
    template_name = "proyectos/proyecto1/part5.html"

class parte6(TemplateView):
    template_name = "proyectos/proyecto1/part6.html"

class parte7(TemplateView):
    template_name = "proyectos/proyecto1/part7.html"

class final(TemplateView):
    template_name = "proyectos/proyecto1/final.html"
