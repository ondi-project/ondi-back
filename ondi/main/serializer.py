from django.contrib.auth.models import *
from rest_framework import generics,serializers
from rest_framework.response import Response
from .models import *
#Main에서 보여지는 것.
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('p_name', 'p_price','p_image','p_date','p_likecount')
#최신순
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'])
        page = self.paginate_queryset(queryset)
        print("Poroduct Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'])
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)

    #카테고리별 : 함수짜놓기...