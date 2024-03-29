from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
