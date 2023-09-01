from django.urls import path
from .views import KategoriList, KategoriDetail, BukuList, BukuDetail

urlpatterns = [
    path('kategori/', KategoriList.as_view(), name='kategori-list'),
    path('kategori/<int:pk>/', KategoriDetail.as_view(), name='kategori-detail'),
    path('buku/', BukuList.as_view(), name='buku-list'),
    path('buku/<int:pk>/', BukuDetail.as_view(), name='buku-detail'),
]
