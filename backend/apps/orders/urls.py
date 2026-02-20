from django.urls import path
from .views import CartView, AddToCartView, CreateOrderView

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/add/", AddToCartView.as_view()),
    path("create-order/", CreateOrderView.as_view()),
]