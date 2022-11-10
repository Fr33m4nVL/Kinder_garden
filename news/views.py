from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post
from .forms import UploadNewsForm

class NewsListView(ListView):
    model = Post
    template_name = 'home.html'

class NewsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewsCreateView(CreateView):
    #model = Post
    form_class = UploadNewsForm
    template_name = 'post_new.html'
    #success_url = reverse('home')
    #fields = ['title', 'body', 'preview', 'image', 'author']

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class NewsEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'preview', 'pictures']

class DeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')