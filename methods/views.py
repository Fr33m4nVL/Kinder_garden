from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Method, File
from .forms import MethodForm

class MethodListView(ListView):
    model = Method
    template_name = 'methods_home.html'

class MethodDetailView(DetailView):
    model = Method
    template_name = 'method_detail.html'

class MethodCreateView(LoginRequiredMixin, CreateView):
    model = Method
    form_class = MethodForm
    template_name = 'method_new.html'
    login_url = 'account_login'

    def post(self, request):
        if request.method == 'POST':
            method = Method.objects.create(
                title=request.POST['title'],
                body=request.POST.get('body'),
                author=request.user
            )

            files = request.FILES.getlist('files')

            for f in files:
                a = File(method=method, file=f)
                a.save()

            return HttpResponseRedirect('/methods/')

class MethodDeleteView(LoginRequiredMixin, DeleteView):
    model = Method
    template_name = 'method_delete.html'
    success_url = reverse_lazy('methods_home')