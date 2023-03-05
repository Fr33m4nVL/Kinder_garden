from django.urls import path

from . import views

urlpatterns = [
    path('add-links/', views.addition_links, name='addition'),
    path('info/', views.garden_info, name='info'),
    path('docs-info/', views.docs_pics, name='docs'),
    path('edu-structure/', views.edu_structure, name='edu_structure'),
    path('edu-standarts/', views.edu_standarts, name='edu_standarts'),
]