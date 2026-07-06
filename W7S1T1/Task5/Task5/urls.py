from django.contrib import admin
from django.urls import path
from Courses import views as courses_views
from Students import views as students_views
from Trainers import views as trainers_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', courses_views.index),
    path('courses', courses_views.index),
    path('students/', students_views.index),
    path('students', students_views.index),
    path('trainers/', trainers_views.index),
    path('trainers', trainers_views.index),
]
