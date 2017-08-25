from django.db import models

# Create your models here.
class curso(models.Model):
    name=models.CharField(max_length=50,help_text='nombre del alumno:')
    phone=models.CharField(max_length=10,help_text='Ingrese el Numero del Alumno:')
    sex=models.CharField(max_length=1,help_text='Ingrse el Tipo de Sexo')
    PubDate=models.DateField(auto_now=True)
