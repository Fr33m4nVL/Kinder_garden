from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(null=True, blank=True)
    preview = models.ImageField(upload_to='previews')
    picture_1 = models.ImageField(upload_to='content', blank=True, null=True)
    picture_2 = models.ImageField(upload_to='content', blank=True, null=True)
    picture_3 = models.ImageField(upload_to='content', blank=True, null=True)
    picture_4 = models.ImageField(upload_to='content', blank=True, null=True)
    picture_5 = models.ImageField(upload_to='content', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])