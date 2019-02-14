from django.db import models
from django.db.models import CharField

# Create your models here.
class Barang(models.Model):
    gambar = models.ImageField(blank=True,null=True,upload_to="")
    judul = models.CharField(max_length=255)
    teks = models.IntegerField()
    def __str__(self):
        return self.judul   