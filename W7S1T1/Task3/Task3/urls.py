from django.contrib import admin
from django.urls import path
from Products import views as products_views
from Orders import views as orders_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_views.index),
    path('products', products_views.index),
    path('orders/', orders_views.index),
    path('orders', orders_views.index),
]
