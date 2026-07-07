from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_doctors, name='get_doctors'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('update/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
]
