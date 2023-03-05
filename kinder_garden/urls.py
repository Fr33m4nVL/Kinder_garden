from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #home
    path('', include('news.urls')),
    #navbar
    path('ped-staff/', include('users.urls')),
    path('other-info/', include('additional_information.urls')),
    path('photoalbums/', include('photoalbum.urls')),
    path('methods/', include('methods.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
