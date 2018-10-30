from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    contrasenia = models.CharField(max_length=100)
    reContrasenia = models.CharField(max_length=100)
    
    def __str__(self):
        return "nombres: "+self.nombres+"apellidos: "+self.apellidos+"email: "+self.email+"contrasenia: "+self.contrasenia+"reContrasenia: "+self.reContrasenia
    
