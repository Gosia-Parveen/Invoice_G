from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('admin-dashboard/', views.admin_dash, name="admin_dash"),
    path('account-manager/', views.acc_man, name="acc_man"),
    path('logout/', views.logout, name="logout"),

    # ----------------------------------------------Subscription---------------------------------------
    path('subscript/', views.subs_tab, name="subs_tab"),
    path("subscript/add/", views.add_subscription,name="add_subscription" ),
    path("subscript/edit/<int:id>/", views.edit_subscription, name="edit_subscription"), 
    path('subscript/archive/<int:id>/',views.archive_subscription,name='archive_subscription'),
    path('archived-subscriptions/', views.view_archived_subscriptions,name='view_archived_subscriptions'),
    path('archived-subscriptions/restore/<int:id>/',views.restore_subscription,name='restore_subscription'),

    # ----------------------------------------------Invoice---------------------------------------
    path('invoices/',views.invoice_list,name='invoice_list'),

    path('invoices/add/',views.add_invoice,name='add_invoice'),

    path('invoices/<int:invoice_id>/edit/',views.edit_invoice,name='edit_invoice'),

    path('invoices/<int:invoice_id>/issue/',views.issue_invoice,name='issue_invoice'),

    path('invoices/<int:invoice_id>/paid/',views.mark_invoice_paid,name='mark_invoice_paid'),

    path('invoices/<int:invoice_id>/void/',views.void_invoice,name='void_invoice'),

    path('invoices/<int:invoice_id>/credit-note/',views.create_credit_note,name='create_credit_note'),

    #--------------------------ALERT----------------------  
    path('admin-dashboard/dismiss-overdue/<int:invoice_id>/',views.dismiss_overdue_alert, name='dismiss_overdue_alert' ),
]
