from django.contrib import admin
from django.urls import path
from Restaurants import views as restaurants_views
from Menu import views as menu_views
from Orders import views as orders_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', restaurants_views.index),
    path('restaurants', restaurants_views.index),
    path('menu/', menu_views.index),
    path('menu', menu_views.index),
    path('orders/', orders_views.index),
    path('orders', orders_views.index),
]
