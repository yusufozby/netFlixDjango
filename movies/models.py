
from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=150)
    def __str__(self):
        return self.isim
class Movies(models.Model):
    kategori = models.ForeignKey(Kategori,on_delete=models.CASCADE,null=True)
    isim = models.CharField(max_length=200,verbose_name="film ismi")
    resim = models.FileField(upload_to="filmler/",verbose_name="film resmi")
    video = models.FileField(upload_to="vidolar/",null=True)
    def __str__(self):
        return self.isim