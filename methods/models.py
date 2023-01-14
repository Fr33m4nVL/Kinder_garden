from django.db import models
from django.contrib.auth import get_user_model

class Method(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

class File(models.Model):
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='documents')