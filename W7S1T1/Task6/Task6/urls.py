from django.contrib import admin
from django.urls import path
from Accounts import views as accounts_views
from Loans import views as loans_views
from Transactions import views as transactions_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', accounts_views.index),
    path('accounts', accounts_views.index),
    path('loans/', loans_views.index),
    path('loans', loans_views.index),
    path('transactions/', transactions_views.index),
    path('transactions', transactions_views.index),
]
