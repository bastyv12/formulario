from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion_fisica = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
