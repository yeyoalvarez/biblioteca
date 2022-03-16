from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_carga = models.DateField('Fecha de Carga',blank=False, null=False)
    signatura = models.CharField(max_length=25, blank=False, null=False)
    titulo = models.CharField('Título', max_length=100, blank=False, null=False)
    autor = models.ManyToManyField('persona')
    autor2 = models.ManyToManyField('persona')
    editorial = models.CharField(max_length=100, blank=False, null=False)
    coleccion = models.CharField(max_length=100,blank=True,null=False)
    edicion = models.CharField(max_length=100, blank=True, null=False)
    isbn = models.CharField(max_length=100, blank=True, null=False)
    lugar_impresion = models.CharField(max_length=100, blank=False, null=False)
    notas = models.TextField(blank=True,max_length=255)
    tema_libro = models.ManyToManyField('libro.temas')
    anho_impresion = models.IntegerField('Año Impresion', blank=False, null=False)
    idioma_libro = models.ManyToManyField('libro.idioma')

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
    descripcion = models.TextField(blank = False, null=False)
    fecha = models.DateField(blank=False, null=False)
    numero_hojas = models.IntegerField(blank = False, null=False)
    lugar_expedicion = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['fecha']

class temas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tema = models.CharField(max_length=25, blank=False, null=False)

    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'Temas'
        ordering = ['nombre_tema']

    def __str__(self):
        return self.nombre_tema

class idioma(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_idioma = models.CharField(max_length=25, blank=False, null=False)

    class Meta:
        verbose_name = 'idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['nombre_idioma']

    def __str__(self):
        return self.nombre_idioma