from django.urls import path
from .views import CategoryListView, ProductListView, ProductVariantListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('variants/', ProductVariantListView.as_view(), name='variant-list'),
]