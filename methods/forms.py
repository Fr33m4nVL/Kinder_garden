from django import forms

from .models import Method

class MethodForm(forms.ModelForm):
    files = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
    class Meta:
        model = Method
        fields = ['title', 'body', 'files']