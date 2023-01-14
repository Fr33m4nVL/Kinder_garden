from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'fathers_name',
            'age',
            'work_experience',
            'photo',
            'additional_information',
            'staff_post',
            'phone_number',
        )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)