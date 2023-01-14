from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Photoalbum(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Текст', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photoalbum_detail', args=[str(self.id)])

class Image(models.Model):
    album = models.ForeignKey(Photoalbum, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='albums')
    image_spec_id = models.IntegerField(null=True, blank=True)