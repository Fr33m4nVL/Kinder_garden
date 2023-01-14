from django.urls import path

from .views import (
    NewsListView,
    NewsDetailView,
    NewsCreateView,
    NewsDeleteView
)

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('post/<int:pk>/', NewsDetailView.as_view(), name='post_detail'),
    path('post/new/', NewsCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
]