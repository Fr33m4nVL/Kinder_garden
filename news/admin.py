from django.contrib import admin

from . import models

class ImageInline(admin.StackedInline):
    model = models.Image
    extra = 0

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]