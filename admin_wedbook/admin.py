from django.contrib import admin

# Register your models here.
from .models import Gallery_Foto,Profil,KomentarSaran



admin.site.register(KomentarSaran)
admin.site.register(Gallery_Foto)
admin.site.register(Profil)