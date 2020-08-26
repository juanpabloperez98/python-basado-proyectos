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


class part5(TemplateView):
    template_name = "proyectos/proyecto3/part5.html"


class part6(TemplateView):
    template_name = "proyectos/proyecto3/part6.html"


class part7(TemplateView):
    template_name = "proyectos/proyecto3/part7.html"


class part8(TemplateView):
    template_name = "proyectos/proyecto3/part8.html"


class final(TemplateView):
    template_name = "proyectos/proyecto3/final.html"
