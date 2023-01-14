from django.shortcuts import render
from django.views.generic import ListView

from .models import Method

class MethodListView(ListView):
    model = Method
    template_name = 'methods.html'