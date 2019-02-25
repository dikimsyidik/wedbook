from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse 
# Create your views here.
from .forms import TambahFoto_Form,Profil_Edit_Form,LoginForm
from .models import Gallery_Foto,Profil
from django.contrib.auth import logout,login,get_user_model

User = get_user_model()

def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard(request):
	form = TambahFoto_Form(request.POST,request.FILES or None)

	if form.is_valid():
		obj = form.save(commit=False)
		print(obj)
		obj.save()
		return HttpResponseRedirect('/dashboard/')

	template = 'admin_rjf/tambah_gallery.html'
	context = {
		'form':form,


	}

	return render(request, template, context)

@login_required
def list_gallery(request):
	images = Gallery_Foto.objects.all()

	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='Rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')
	template = 'admin_rjf/list_gallery.html'
	print(request.user.is_authenticated)
	profil = Profil.objects.all()




	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'images':images,
		'profil':profil,

		}
	return render(request, template, context)

@login_required
def hapus_foto(request,list_gallery_id):
	objectnya =  Gallery_Foto.objects.get(id=list_gallery_id)
	
	objectnya.delete()	

	return HttpResponseRedirect('/dashboard/')

@login_required
def profil_edit(request, id=None):
    obj = get_object_or_404(Profil, id=id)
    form = Profil_Edit_Form(request.POST or None, instance=obj)
	    
    context = {
        "form": form
    }
    if form.is_valid():
    	form = Profil_Edit_Form(request.POST,request.FILES or None, instance=obj)
    	obj = form.save(commit=True)
    	print(obj)
    	obj.save()
    	return HttpResponseRedirect('/dashboard/')
    template = "admin_rjf/edit2.html"
    return render(request, template, context)


