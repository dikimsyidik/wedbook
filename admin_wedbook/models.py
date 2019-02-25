from django.db import models
# Create your models here.
import os
from django.dispatch import receiver

 
KATEGORI_PRODUK = [
        ('backdrop', 'Back Drop'),
        ('bedroom', 'Bedroom'),
        ('meja_meeting', 'Meja Meeting'),
        ('front_office', 'Front Office'),
		('rak', 'Rak'),
		('tangga','Tangga'),

    ]


def path_and_rename(instance, filename):
    return (str(instance)+".jpg")


class KomentarSaran(models.Model):
	nama = models.CharField(max_length=200)
	no_hp = models.CharField(max_length=15)
	email = models.EmailField(blank=True)
	pesan = models.TextField()

	def __str__(self):
		return self.nama

class Gallery_Foto(models.Model):
	"""docstring for Produk"""
		

	produk = models.CharField(max_length=200)
	post_thumbnail  = models.ImageField(default='default.jpg', upload_to=path_and_rename)
	kategori = models.CharField(max_length=200,choices=KATEGORI_PRODUK)
	


	def __str__(self):
		return self.produk
class Profil(models.Model):
	# tentang kami 
	nama_profil = models.CharField(max_length=100,default='profilnya')

	foto_perusahaan = models.ImageField(default='default.jpg', upload_to=path_and_rename)
	deskripsi_perusahaan = models.TextField()
	
	#produk unggulan
	

	#kontak

	alamat = models.CharField(max_length=100)

	no_hp = models.CharField(max_length=100)
	whatsapp =models.CharField(max_length=100)

	email = models.EmailField(max_length=100)

	#media sosial
	facebook = models.URLField()
	twitter = models.URLField()
	instagram =  models.URLField()
	google_plus =  models.URLField()

	def __str__(self):
		return self.nama_profil

	


