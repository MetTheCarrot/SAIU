from django.db import models

# Create your models here.

class Septiembre(models.Model):
    class Meta:
        verbose_name = "Septiembre"
        verbose_name_plural = "Septiembre"
    id = models.AutoField(primary_key=True)
    primeraSemana = models.IntegerField(verbose_name="Semana 1")
    segundaSemana = models.IntegerField(verbose_name="Semana 2")
    terceraSemana = models.IntegerField(verbose_name="Semana 3")
    cuartaSemana = models.IntegerField(verbose_name="Semana 4")
    # def __str__(self):
    #     return self.name


class Octubre(models.Model):
    class Meta:
        verbose_name = "Octubre"
        verbose_name_plural = "Octubre"
    id = models.AutoField(primary_key=True)
    primeraSemana = models.IntegerField(verbose_name="Semana 1")
    segundaSemana = models.IntegerField(verbose_name="Semana 2")
    terceraSemana = models.IntegerField(verbose_name="Semana 3")
    cuartaSemana = models.IntegerField(verbose_name="Semana 4")
    # def __str__(self):
    #     return self.name


class Noviembre(models.Model):
    class Meta:
        verbose_name = "Noviembre"
        verbose_name_plural = "Noviembre"
    id = models.AutoField(primary_key=True)
    primeraSemana = models.IntegerField(verbose_name="Semana 1")
    segundaSemana = models.IntegerField(verbose_name="Semana 2")
    terceraSemana = models.IntegerField(verbose_name="Semana 3")
    cuartaSemana = models.IntegerField(verbose_name="Semana 4")
    # def __str__(self):
    #     return self.name
