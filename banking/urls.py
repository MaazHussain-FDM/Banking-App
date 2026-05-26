from django.urls import path

from . import views

urlpatterns = [
    path("", views.account_detail, name="account-detail"),
    path("register/", views.register_view, name="register"),
    path("deposit/", views.deposit_view, name="deposit"),
    path("withdraw/", views.withdraw_view, name="withdraw"),
    path("transactions/", views.transaction_list_view, name="transactions"),
]

