from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)

class proyecto3(TemplateView):
    template_name = "proyectos/proyecto3/index.html"

class part1(TemplateView):
    template_name = "proyectos/proyecto3/part1.html"

class part2(TemplateView):
    template_name = "proyectos/proyecto3/part2.html"

class part3(TemplateView):
    template_name = "proyectos/proyecto3/part3.html"

class part4(TemplateView):
    template_name = "proyectos/proyecto3/part4.html"