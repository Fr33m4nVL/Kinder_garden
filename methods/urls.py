from django.urls import path

from . import views

urlpatterns = [
    path('', views.MethodListView.as_view(), name='methods_home'),
    path('<int:pk>/', views.MethodDetailView.as_view(), name='method_detail'),
    path('new/', views.MethodCreateView.as_view(), name='method_new'),
    path('<int:pk>/delete/', views.MethodDeleteView.as_view(), name='method_delete'),
]