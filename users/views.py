from django.shortcuts import render
from django.contrib.auth import get_user_model
#from django.views.generic import ListView

from .models import CustomUser

#class ProfileListView(ListView):
    #user = get_user_model()
    #model = CustomUser
    #template_name = 'staff_list.html'

def profile_list_view(request):
    users = get_user_model().objects.filter(is_superuser=False)
    return render(request, 'staff_list.html', {'users': users})
