from django.contrib import admin
from django.urls import path
from Doctor import views as doctor_views
from Patient import views as patient_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', doctor_views.index),
    path('doctor', doctor_views.index),
    path('patient/', patient_views.index),
    path('patient', patient_views.index),
]
