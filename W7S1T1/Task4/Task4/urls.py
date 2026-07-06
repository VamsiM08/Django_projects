from django.contrib import admin
from django.urls import path
from Books import views as books_views
from Members import views as members_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_views.index),
    path('books', books_views.index),
    path('members/', members_views.index),
    path('members', members_views.index),
]
