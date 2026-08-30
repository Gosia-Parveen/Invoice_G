from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('admin-dashboard/', views.admin_dash, name="admin_dash"),
    path('account-manager/', views.acc_man, name="acc_man"),
]
