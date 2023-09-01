from django.contrib import admin

# Register your models here.
from .models import Kategori, Buku

admin.site.register(Kategori)
admin.site.register(Buku)