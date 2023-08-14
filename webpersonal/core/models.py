from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    memoria = models.CharField(null=True, blank=True, max_length=100, verbose_name="Memoria")
    version = models.CharField(null=True, blank=True, max_length=100, verbose_name="Versión")
    procesador = models.CharField(null=True, blank=True, max_length=100, verbose_name="Procesador")
    bateria = models.CharField(null=True, blank=True, max_length=100, verbose_name="Batería")
    camara = models.CharField(null=True, blank=True, max_length=100, verbose_name="Cámara")
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ["-created"]

    def __str__(self):
        return self.title
