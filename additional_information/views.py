from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def addition_links(request):
    return render(request, template_name='addition.html')