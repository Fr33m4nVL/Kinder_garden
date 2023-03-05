from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Post, Image
from .forms import PostForm

class NewsListView(ListView):
    model = Post
    template_name = 'home.html'

class NewsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    login_url = 'account_login'

    def post(self, request):
        if request.method == 'POST':
            post = Post.objects.create(
                title=request.POST['title'],
                body=request.POST['body'],
                preview=request.FILES['preview'],
                author=request.user
            )
            images = request.FILES.getlist('images')

            for f in images:
                a = Image(post=post, image=f)
                a.save()
            #return reverse('post_detail', args=[str(post.pk)])
            return HttpResponseRedirect('/')


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')