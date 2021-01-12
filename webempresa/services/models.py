from django.db import models

# Create your models here.
class Service(models.Model):
    
    title = models.CharField(max_length=200, verbose_name='titulo')
    subtitle = models.CharField(max_length=200, verbose_name='subtitulo')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to='services') #el upload es para indicar donde subir la imagen
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación') #auto_now para crear la fecha automaticamente
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural= 'servicios'
        ordering = ['-created'] #con el menos por delante significa ordenar de forma descendente
    
    def __str__(self):
        return self.title
