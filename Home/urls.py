from django.urls import path
from . import views

urlpatterns = [
    path('', views.BarangPost, name='Barang'),
    path('input/', views.Barang_Input, name='BarangInput'),
    path('<int:barang_id>/', views.Barang_Detail, name='BarangDetail'),
    
]


