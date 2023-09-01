# serializers.py
from rest_framework import serializers
from .models import Kategori, Buku

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    kategori = serializers.SerializerMethodField()
    
    def get_kategori(self, obj):
        return {
            'id': obj.kategori.id,
            'nama_kategori': obj.kategori.nama_kategori,
        }

    class Meta:
        model = Buku
        fields = ['id', 'nama_buku', 'penerbit', 'tahun_terbit', 'kategori']
        # fields = '__all__'
