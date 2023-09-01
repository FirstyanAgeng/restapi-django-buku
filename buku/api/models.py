from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=255)
    class Meta:
        ordering = ['nama_kategori']
        verbose_name_plural = 'Kategoris'

    def __str__(self):
        return self.nama_kategori

class Buku(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama_buku = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    tahun_terbit = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nama_buku
    
    @property
    def nama_kategori(self):
        return self.kategori.nama_kategori
