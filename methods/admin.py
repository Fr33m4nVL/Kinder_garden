from django.contrib import admin

from . import models

class FileInline(admin.StackedInline):
    model = models.File
    extra = 0

@admin.register(models.Method)
class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline]