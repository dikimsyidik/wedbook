from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import Pasangan,Vendor,dasboard,my_produk,tambah_produk,pesanan,reviews
from django.urls import path

urlpatterns = [
    # url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    # url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    # url(r"pasangan/$", Pasangan.as_view(), name="pasangan_daftar"),
    path('pasangan_daftar/',Pasangan.as_view(),name='pasangan_daftar'),
    path('vendor_daftar/',Vendor.as_view(),name='vendor_daftar'),
    path('dashboard_vendor/',dasboard,name='dashboard_vendor'),
    path('my_produk/',my_produk,name='my_produk'),
    path('tambah_produk/',tambah_produk,name='tambah_produk'),
    path('pesanan/',pesanan,name='pesanan'),
    path('reviews/',reviews,name='reviews'),
 



]
