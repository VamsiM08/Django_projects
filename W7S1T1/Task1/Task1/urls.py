from django.contrib import admin
from django.urls import path
from Employee import views as employee_views
from Department import views as department_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee_views.index),
    path('employee', employee_views.index),
    path('department/', department_views.index),
    path('department', department_views.index),
]
