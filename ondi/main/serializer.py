from django.contrib.auth.models import *
from rest_framework import generics,serializers
from rest_framework.response import Response
from .models import *
from django.db.models import Q

class NProductListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ('id', 'p_name', 'p_price','p_image','p_date','p_viewcount','p_likecount','p_tag')

#Main에서 보여지는 것.#최신순
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','p_name', 'p_price','p_image','p_date','p_viewcount','p_likecount','p_tag') #로그인한 내가 좋아한지여부 추가해줘야함!
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(p_buy = False)
    serializer_class = ProductListSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'],reverse=True)
        page = self.paginate_queryset(queryset)
        print("Product Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'],reverse=True)
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)

#카테고리별 (카테고리, 조회option 입력받아야함)
class CategoryListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    def list(self, request, category, view_option):
        # 'p_keyword' 'p_likecount' 'p_viewcount' 'p_date'
        if view_option == 'p_likecount':
            option = 'p_likecount'
        elif view_option == 'p_viewcount':
            option = 'p_viewcount'
        elif view_option == 'p_date':
            option = 'p_date'
        print(option)
        self.queryset = Product.objects.filter(p_category=category)
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x[option], reverse=True)
        page = self.paginate_queryset(queryset)
        print("Product Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x[option], reverse=True)
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)

#검색화면 (검색어 입력받아야함)
class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    def list(self, request, product_search):
        self.queryset = Product.objects.filter(Q(p_tag__contains = product_search)|Q(p_name__contains = product_search))
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'], reverse=True)
        page = self.paginate_queryset(queryset)
        print("Product Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'], reverse=True)
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)


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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  '__all__'
        # fields = ('id','p_name', 'p_price','p_image','p_date','p_viewcount','p_likecount','p_tag') #로그인한 내가 좋아한지여부 추가해줘야함!
#개별product view
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def list(self, request, product_id,user_id):
        # 조회수올리기
        product = Product.objects.get(id=product_id)
        before_value = product.p_viewcount
        after = (int(before_value) + 1)
        product.p_viewcount = (after)
        product.save()
        # Like여부확인
        user = User.objects.get(id=user_id)
        print(user_id)
        # p_like =False
        try:
            print('like')
            like = Like.objects.filter(from_user=user, product=product)
            if like[0]:
                p_like = True
        except:
            p_like = False
        # 상품보내주기
        self.queryset = Product.objects.filter(id= product_id)
        #livebutton설정
        if user_id == self.queryset[0].p_seller.id:
            livebutton = True
        else:
            livebutton = False
            
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'], reverse=True)
        sorted_serializer_data.append({'like':p_like, 'livebutton': livebutton})
        page = self.paginate_queryset(queryset)
        print("Product Work", page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sorted_serializer_data = sorted(serializer.data, key=lambda x: x['p_date'], reverse=True)
            return self.get_paginated_response(sorted_serializer_data)
        return Response(sorted_serializer_data)