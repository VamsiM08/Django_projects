from django.urls import path
from . import views

urlpatterns = [
    # Template URLs
    path('', views.doctor_home, name='doctor_home'),
    path('details/', views.doctor_details, name='doctor_details'),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('contact/', views.doctor_contact, name='doctor_contact'),

    # REST API URLs
    path('api/', views.doctor_home_api, name='doctor_home_api'),
    path('api/details/', views.doctor_details_api, name='doctor_details_api'),
    path('api/add/', views.add_doctor_api, name='add_doctor_api'),
    path('api/update/', views.update_doctor_api, name='update_doctor_api'),
    path('api/delete/', views.delete_doctor_api, name='delete_doctor_api'),

    # Dynamic URLs (must come after static paths to avoid overrides)
    path('<int:doctor_id>/', views.doctor_by_id, name='doctor_by_id'),
    path('<str:doctor_name>/', views.doctor_by_name, name='doctor_by_name'),
]
