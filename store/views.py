from django.shortcuts import render, get_object_or_404
from .models import Beat, Categoria

def home(request):
    categorias = Categoria.objects.all()
    beats = Beat.objects.select_related('categoria').all()
    context = {
        'categorias': categorias,
        'beats': beats,
    }
    return render(request, 'store/home.html', context)

def categoria_view(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    categorias = Categoria.objects.all()
    beats = Beat.objects.filter(categoria=categoria)
    context = {
        'categoria_actual': categoria,
        'categorias': categorias,
        'beats': beats,
    }
    return render(request, 'store/category.html', context)

def beat_detalle(request, pk):
    categorias = Categoria.objects.all()
    beat = get_object_or_404(Beat, pk=pk)
    context = {
        'categorias': categorias,
        'beat': beat,
    }
    return render(request, 'store/detail.html', context)
