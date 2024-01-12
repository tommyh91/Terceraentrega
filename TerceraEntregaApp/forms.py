from django import forms
from .models import alumno, curso, entrega

class alumnoForm(forms.ModelForm):
    class Meta:
        model = alumno
        fields = '__all__'

class cursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = '__all__'

class entregaForm(forms.ModelForm):
    class Meta:
        model = entrega
        fields = '__all__'
