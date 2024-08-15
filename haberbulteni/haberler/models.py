from django.db import models

class Makale(models.Model):
	yazar = models.CharField(max_length=150)
	baslik = models.CharField(max_length=150)
	aciklama = models.CharField(max_length=150)
	metin = models.TextField()
	sehir = models.CharField(max_length=150)
	yayimlanma_tarihi = models.DateField()
	aktif = models.BooleanField(default=True)
	yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
	guncelleme_tarihi = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.baslik
