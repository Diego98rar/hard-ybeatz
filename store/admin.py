from django.contrib import admin
from .models import Categoria, Beat

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio', 'stock', 'creado_en')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'descripcion')
