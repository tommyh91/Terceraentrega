from django.db import models

# Create your models here.

class alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

class curso(models.Model):
    nombr_curso = models.CharField(max_length=50)
    numero_comision = models.IntegerField()
    

class entrega(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    