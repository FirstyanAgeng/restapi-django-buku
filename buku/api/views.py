from rest_framework import generics
from .models import Kategori, Buku 
from .serializers import KategoriSerializer, BukuSerializer

class KategoriList(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class KategoriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class BukuList(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class BukuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer