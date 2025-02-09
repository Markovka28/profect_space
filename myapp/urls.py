from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('object/create/', views.object_create, name='object_create'),
    path('object/list/', views.object_list, name='object_list'),
]
