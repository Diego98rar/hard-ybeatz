from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoría', max_length=50, unique=True)
    slug = models.SlugField('Identificador (slug)', max_length=60, unique=True, blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'        
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Beat(models.Model):
    titulo = models.CharField('Título del beat', max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='beats')
    precio = models.DecimalField('Precio (CLP)', max_digits=8, decimal_places=2)  
    stock = models.PositiveIntegerField('Stock disponible', default=1)   
    descripcion = models.TextField('Descripción del beat', blank=True)
    imagen = models.ImageField('Carátula', upload_to='beats/')
    bpm = models.PositiveIntegerField('BPM', default=120)
    key = models.CharField('Key', max_length=12, blank=True)
    creado_en = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Beat'
        verbose_name_plural = 'Beats'
        ordering = ['-creado_en']

    def __str__(self):
        return self.titulo
