from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        product = self.queryset.get(pk=kwargs.get('pk'))
        product.view_count += 1
        product.save()
        serializer = self.get_serializer()
        print(serializer)
        return self.retrieve(request, *args, **kwargs)
