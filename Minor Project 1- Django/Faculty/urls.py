from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty, name='faculty'),
    path('details/', views.faculty_details, name='faculty_details'),
    path('profile/', views.faculty_profile, name='faculty_profile'),
    path('<str:name>/', views.faculty_name, name='faculty_name'),
]
