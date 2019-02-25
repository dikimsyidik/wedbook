from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
from admin_wedbook.models import Gallery_Foto,Profil
from admin_wedbook.forms import FormKomentar
from blog.models import PostModel
def index(requset):
	
	profil = Profil.objects.all()

	template = 'basic/index.html'
	context = {
		'profil':profil,
		}

	return render(requset,template,context)
def tentang_kami(requset):
	
	profil = Profil.objects.all()


	
	template = 'basic/blog-listing.html'
	context = {
		'profil':profil,
		
		}

	return render(requset,template,context)
def blog_listing(request):
    artikelnya = PostModel.objects.all().order_by('-publish_date')[:5]
    profil = Profil.objects.all()
    list_blog = PostModel.objects.all()
    paginator = Paginator(list_blog, 4)



    page = request.GET.get('page',1)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)



    context = {
		'blog':blog,
		'profil':profil,
		"artikels":artikelnya,
		}
    template = 'basic/blog-listing.html'
    return render(request,template,context)



def team(requset):
    artikelnya = PostModel.objects.all().order_by('-publish_date')[:5]
    list_blog = PostModel.objects.all()
    profil = Profil.objects.all()
    context = {
		'blog':list_blog,
		'profil':profil,
		"artikels":artikelnya,
		}
    template = 'basic/team-page.html'
    return render(requset,template,context)



def list_produk(request):
	profil = Profil.objects.all()


	context = {
		'profil':profil,
		}	
	template = 'basic/list-produk.html'

	return render(request,template,context)




def contact(request):
	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='Rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')
	form = FormKomentar(request.POST or None)



		
	template = 'basic/contact-us.html'
	profil = Profil.objects.all()


	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/')



	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'profil':profil,
		'form':form,
		}

	print(type(rak))
	print(bedroom)

	return render(request,template,context)
