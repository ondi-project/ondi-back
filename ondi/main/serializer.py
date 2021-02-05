from django.contrib.auth.models import *
from rest_framework import generics,serializers
from rest_framework.response import Response
from .models import *
#Main에서 보여지는 것.#최신순
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','p_name', 'p_price','p_image','p_date','p_likecount','p_viewcount')
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(p_buy = False)
    serializer_class = ProductListSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'])
        page = self.paginate_queryset(queryset)
        print("Product Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'])
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)

    #카테고리별 : 함수짜놓기...


#LiveList에서 보여지는것
class LiveListSerializer(serializers.ModelSerializer):
    l_product =ProductListSerializer(read_only =True)
    class Meta:
        model = LiveProduct
        fields = ('id','l_date', 'l_product','l_sprice')
class LiveListView(generics.ListAPIView):
    queryset = LiveProduct.objects.all()
    serializer_class = LiveListSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['l_date'])
        page = self.paginate_queryset(queryset)
        print("Live Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key = lambda x: x['l_date'])
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)

    #카테고리별 : 함수짜놓기...




