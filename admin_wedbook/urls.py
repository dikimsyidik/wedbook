from django.urls import path
from .views import (
    dashboard,
    list_gallery,
    hapus_foto,
    profil_edit,
   
  
    )

urlpatterns = [
    path('tambah_gallery/', dashboard, name='tambah_foto'),
    path('', list_gallery, name='dashboard'),
    path('hapus/<int:list_gallery_id>', hapus_foto, name='hapus_foto'),
    path('<int:id>', profil_edit, name='profil_edit'),
  


    # url(r'^tambah2/$', tambahpaket30, name='paket30'),
    # url(r'^hapus/(?P<id>\d+)$', hapus_kelas_private, name='hapust-private'),
    # url(r'^pendaftar/$', english_course_pendaftar, name='pendaftar'),
    # url(r'^create/$', post_model_create_view, name='create'),
    # url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    # url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name='delete'),
    # url(r'^pendaftar/(?P<id>\d+)$', english_update_view, name='update'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', home, name='home'),
    #url(r'^redirect/$', redirect_somewhere, name='home')
]
