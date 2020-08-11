from django.shortcuts import render

# Create your views here.

from django.views.generic import(
    TemplateView
)

class home(TemplateView):
    template_name = "teoria/moduls/graficos/graficos.html"

class tkinter(TemplateView):
    template_name = "teoria/moduls/graficos/tkinter.html"

class firts_gui(TemplateView):
    template_name = "teoria/moduls/graficos/firts_gui.html"

class frames(TemplateView):
    template_name = "teoria/moduls/graficos/frames.html"

class labels(TemplateView):
    template_name = "teoria/moduls/graficos/labels.html"
