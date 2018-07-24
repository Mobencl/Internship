from django import forms
from SportcenterApp.models import Photo

class PhotoForms(forms.ModelForm):
    model = Photo
    fields = ['path',]
