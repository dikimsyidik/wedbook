from django.db import models

# Create your models here.




class Product(models.Model):
	
	nama_produk = models.CharField(max_length=300)
	kategori = models.CharField(max_length=300)
	harga = models.CharField(max_length=300)
	alamat = models.CharField(max_length=300)
	kota = models.CharField(max_length=300)
	provinsi =models.CharField(max_length=300)
	deskripsi = models.TextField()
	foto_produk = models.ImageField(max_length=300)
	video = models.CharField(max_length=300)

	def __str__():
		pass
