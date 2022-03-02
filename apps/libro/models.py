from django.db import models

# Create your models here.


class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    autor = models.CharField('Autor principal',max_length=100, blank=False, null=False)
    autor2 = models.CharField('Segundo Autor',blank=True,max_length=100)
    fecha_impresion = models.DateField('Fecha de Impresion',blank=False, null=False)
    editorial = models.CharField(max_length=100, blank=False, null=False)
    coleccion = models.CharField(max_length=100, null=False)
    edicion = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=100, blank=False, null=False)
    lugar_impresion = models.CharField(max_length=100, blank=False, null=False)
    notas = models.TextField(blank=True,max_length=255)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class archivo(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=255, blank=False, null=False)
    subserie = models.CharField(max_length=255, blank=False, null=False)
    subserie = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField(blank = False, null=False)
    fecha = models.DateField(blank=False, null=False)
    numero_hojas = models.IntegerField(blank = False, null=False)
    lugar_expedicion = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['fecha']
