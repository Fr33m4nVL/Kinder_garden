from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

class NewsListView(ListView):
    model = Post
    template_name = 'home.html'

class NewsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewsCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'preview', 'image', 'author']


class NewsEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'preview', 'pictures']

class DeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')