from django.contrib import admin
from django.urls import path
from Students import views as students_views
from Teachers import views as teachers_views
from Classes import views as classes_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', students_views.index),
    path('students', students_views.index),
    path('teachers/', teachers_views.index),
    path('teachers', teachers_views.index),
    path('classes/', classes_views.index),
    path('classes', classes_views.index),
]
