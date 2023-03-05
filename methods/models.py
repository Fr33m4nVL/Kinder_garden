import os
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Method(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('method_detail', args=[str(self.id)])

class File(models.Model):
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents')