from django.urls import path

from .views import addition_links

urlpatterns = [
    path('add-links/', addition_links, name='addition'),
]