from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import alumnoForm, cursoForm, entregaForm

# Create your views here.


class alumnoFormView(FormView):
    template_name = 'clase1_form.html'
    form_class = alumnoForm
    success_url = '/'

class cursoFormView(FormView):
    template_name = 'clase2_form.html'
    form_class = cursoForm
    success_url = '/'

class entregaFormView(FormView):
    template_name = 'clase3_form.html'
    form_class = entregaForm
    success_url = '/'