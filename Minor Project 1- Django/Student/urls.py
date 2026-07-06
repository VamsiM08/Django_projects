from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('details/', views.student_details, name='student_details'),
    path('profile/', views.student_profile, name='student_profile'),
    path('<int:id>/', views.student_id, name='student_id'),
]
