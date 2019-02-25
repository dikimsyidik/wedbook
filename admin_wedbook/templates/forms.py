from django import forms


from .models import CourseEnglish,PrivateCLass,RegularClass


class CourseEnglishForm(forms.ModelForm):
    class Meta:
        model = CourseEnglish
        fields = [
            'nama',
            'no_hp',
            'alamat',
            'asal_sekolah',
            'pilihan_program',
            'jenis_kelas',
            'pembayaran',
        ]
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'input-field','name':'Nama'}),
            'alamat': forms.Textarea(attrs={'class': 'textarea'}),
        }
