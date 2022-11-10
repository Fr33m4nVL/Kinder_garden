from django import forms
from multiupload.fields import MultiImageField

from .models import Post

class UploadNewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'preview', 'author']

    images = MultiImageField(max_num=20)

    def save(self, commit=True):
        instance = super(UploadNewsForm, self).save(commit)
        for each in self.cleaned_data['images']:
            Post.objects.create(image=each, post=instance)

        return instance