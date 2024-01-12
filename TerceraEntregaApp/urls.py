from django.urls import path
from .views import alumnoFormView, cursoFormView, entregaFormView

urlpatterns = [
    path('clase1/', alumnoFormView.as_view(), name='alumno_form'),
    path('clase2/', cursoFormView.as_view(), name='curso_form'),
    path('clase3/', entregaFormView.as_view(), name='entrega_form'),
]     