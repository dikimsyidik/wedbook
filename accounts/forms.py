from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms



class DaftarPasanganForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
        widgets = {
        'username':forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
        'email':forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pasangan = True
        if commit:
            user.save()
        return user



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
class DaftarVendorForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
        widgets = {
        'username':forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
        'email':forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
        return user




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"