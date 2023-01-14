from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Photoalbum, Image
from .forms import PhotoalbumForm

class PhotoalbumListView(ListView):
    model = Photoalbum
    template_name = 'photoalbum_home.html'

class PhotoalbumDetailView(DetailView):
    model = Photoalbum
    template_name = 'photoalbum_detail.html'

class PhotoalbumCreateView(LoginRequiredMixin, CreateView):
    model = Photoalbum
    form_class = PhotoalbumForm
    template_name = 'photoalbum_new.html'
    login_url = 'account_login'

    def post(self, request):
        if request.method == 'POST':
            id_number = 0
            photoalbum = Photoalbum.objects.create(
                title=request.POST['title'],
                description=request.POST.get('description', False),
                author=request.user
            )
            images = request.FILES.getlist('images')

            for f in images:
                id_number += 1
                a = Image(album=photoalbum, image=f, image_spec_id=id_number)
                a.save()

            return HttpResponseRedirect('/photoalbums/')