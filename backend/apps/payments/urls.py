from django.urls import path
from .views import CreatePaymentView, ConfirmPaymentView

urlpatterns = [
    path("create/", CreatePaymentView.as_view()),
    path("confirm/", ConfirmPaymentView.as_view()),
]