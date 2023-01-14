from django.contrib import admin

from .models import Photoalbum, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

@admin.register(Photoalbum)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]