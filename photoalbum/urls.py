from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhotoalbumListView.as_view(), name='photoalbum_home'),
    path('<int:pk>/', views.PhotoalbumDetailView.as_view(), name='photoalbum_detail'),
    path('new/', views.PhotoalbumCreateView.as_view(), name='photoalbum_new'),
]