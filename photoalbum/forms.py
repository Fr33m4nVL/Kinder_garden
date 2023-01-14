from django import forms

from .models import Photoalbum

class PhotoalbumForm(forms.ModelForm):
    images = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Photoalbum
        fields = ['title', 'description', 'images']