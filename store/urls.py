from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<slug:slug>/', views.categoria_view, name='categoria'),
    path('beat/<int:pk>/', views.beat_detalle, name='detalle'),
]
