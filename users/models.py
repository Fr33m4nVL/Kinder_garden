from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fathers_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    work_experience = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos', blank=True)
    additional_information = models.TextField(null=True, blank=True)
    staff_post = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)