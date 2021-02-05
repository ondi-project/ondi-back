from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self, *args, **kwargs):
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        products = Product.objects.all()
        if category:
            products = products.filter(category_id=category)
        if name:
            products = products.filter(name__icontains=name)
        return products

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        product = self.queryset.get(pk=kwargs.get('pk'))
        product.view_count += 1
        product.save()
        return self.retrieve(request, *args, **kwargs)
