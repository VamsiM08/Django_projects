from django.urls import path
from . import views

urlpatterns = [
    # Template URLs
    path('', views.patient_home, name='patient_home'),
    path('details/', views.patient_details, name='patient_details'),
    path('report/', views.patient_report, name='patient_report'),
    path('bill/', views.patient_bill, name='patient_bill'),

    # REST API URLs
    path('api/', views.patient_home_api, name='patient_home_api'),
    path('api/details/', views.patient_details_api, name='patient_details_api'),
    path('api/add/', views.add_patient_api, name='add_patient_api'),
    path('api/update/', views.update_patient_api, name='update_patient_api'),
    path('api/delete/', views.delete_patient_api, name='delete_patient_api'),

    # Dynamic URLs (must come after static paths to avoid overrides)
    path('<int:patient_id>/', views.patient_by_id, name='patient_by_id'),
    path('<str:patient_name>/', views.patient_by_name, name='patient_by_name'),
]
