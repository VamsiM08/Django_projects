from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_appointments, name='get_appointments'),
    path('add/', views.add_appointment, name='add_appointment'),
    path('update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
]
