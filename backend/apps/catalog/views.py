from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductVariantListView(generics.ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

    