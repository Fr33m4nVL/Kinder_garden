from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import MainInfo

@login_required
def addition_links(request):
    return render(request, template_name='addition.html')

def garden_info(request):
    main_info = MainInfo.objects.all()
    context = {
        'main_info': main_info,
    }
    return render(request, template_name='info.html', context=context)

def docs_pics(request):
    return render(request, template_name='docs.html')

def edu_standarts(request):
    return render(request, template_name='edu_standarts.html')

def edu_structure(request):
    return render(request, template_name='edu_structure.html')