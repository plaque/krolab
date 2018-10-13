from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/<int:id>', views.category, name='category'),
]
