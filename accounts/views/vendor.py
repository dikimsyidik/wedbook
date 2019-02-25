from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from . import forms


class Vendor(CreateView):
    form_class = forms.DaftarVendorForm
    success_url = reverse_lazy("home")
    template_name = "accounts/vendor-form-register.html"
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


@login_required
def dasboard(request):
	templates = 'dashboard/vendor/vendor-dashboard-overview.html'
	context= {}
	return render(request,templates,context)
@login_required
def my_produk(request):
	templates = 'dashboard/vendor/vendor-dashboard-listing.html'
	context= {}
	return render(request,templates,context)
@login_required
def tambah_produk(request):
	templates = 'dashboard/vendor/vendor-dashboard-add-listing.html'
	context= {}
	return render(request,templates,context)
@login_required
def pesanan(request):
	templates = 'dashboard/vendor/vendor-dashboard-request-quote.html'
	context= {}
	return render(request,templates,context)
@login_required
def reviews(request):
	templates = 'dashboard/vendor/vendor-dashboard-reviews.html'
	context= {}
	return render(request,templates,context)
