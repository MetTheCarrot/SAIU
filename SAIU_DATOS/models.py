from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Info(models.Model):
    class Meta:
        verbose_name = "Información"
        verbose_name_plural = "Información"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return self.name