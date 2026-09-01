from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),

    path('admin-dashboard/', views.admin_dash, name="admin_dash"),
    path('account-manager/', views.acc_man, name="acc_man"),
    path('subscript/', views.subs_tab, name="subs_tab"),
    path("subscript/add/", views.add_subscription,name="add_subscription" ),
    path("subscript/edit/<int:id>/", views.edit_subscription, name="edit_subscription"), 

    path('logout/', views.logout, name="logout"),
]
