from django.shortcuts import render
from rest_framework import generics,serializers
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import simplejson
from django.template.defaulttags import register
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

#Main화면 : 상품들 최신순으로 보여짐
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(p_buy = False).order_by('-p_date')
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
# @method_decorator(csrf_exempt,name='dispatch')
# def main(request):
#     if request.method == "GET":
#         return ProductListView.as_view()(request)


#LiveList화면 : Live들 최근예정순으로 보여짐

@method_decorator(csrf_exempt,name='dispatch')
def livelist(request):
    if request.method == "GET":
        return LiveListView.as_view()(request)

#카테고리화면 :
@method_decorator(csrf_exempt,name='dispatch')
def category(request):
    if request.method == "GET":
        product_category = request.GET.get('p_category')
        product_view_option= request.GET.get('view_option') #'p_keyword' 'p_likecount' 'p_viewcount' 'p_date'
        #############삭제해야함###########3
        if product_category ==None:
            product_category='의류'
        if product_view_option ==None or product_view_option =='p_keyword':
            product_view_option ='p_likecount'
        ###############
        # #카테고리정보를 받으면
        return CategoryListView.as_view()(request,product_category,product_view_option)

#검색화면
@method_decorator(csrf_exempt,name='dispatch')
def search(request):
    if request.method == "GET":
        product_search = request.GET.get('p_search')
        #############삭제해야함###########3
        if product_search ==None:
            product_search='상품'
        ###############
        # 검색어를 받으면
        return SearchListView.as_view()(request,product_search)
    
    
#상품등록화면 : {'p_category':--,'p_name',p_price,p_content,p_image,p_tag,p_nego,p_date,p_likecount,p_seller,p_live}
@method_decorator(csrf_exempt,name='dispatch')
def post(request):
    # if request.method == "GET":
    #     print('get')
    #     return HttpResponse(simplejson.dumps({"response": "GET"}))
    if request.method == "POST":
        print('post')
        image = request.FILES['p_image']
        # request.GET.get('')
        req = json.loads(request.body.decode('utf-8'))
        category = request.POST.get('p_category',None)
        name = request.POST.get('p_name',None)
        price = request.POST.get('p_price',None)
        content = request.POST.get('p_content',None)
        tag = request.POST.get('p_tag',None) #리스트형식
        nego = request.POST.get('p_nego',None) #True ,False형태로
        seller_id = request.POST.get('p_seller',None) #전화번호로 ?아마
        seller = User.objects.get(id=seller_id)

        if req != "None":
            print("POST 데이터를 정상적으로 입력받았습니다")
            poster = Product(p_category=category, p_name=name, p_price=price,p_content=content,p_tag=tag,p_nego=nego,p_likecount=0, p_seller =seller,p_live=None)
            poster.p_image=image
            poster.p_date=timezone.now()
            poster.save()
            return HttpResponse(simplejson.dumps({"response": "Good"}))
        else:
            print("POST 데이터를 찾을 수 없습니다")
            return HttpResponse(simplejson.dumps({"response": "Fail"}))

@method_decorator(csrf_exempt,name='dispatch')
def view_product(request):
    if request.method == "GET":
        # 특정상품보여주기!
        product_id = request.GET.get('p_id')
        user_id = request.GET.get('u_id')
        ##########없애줘야힘
        if product_id ==None:
            product_id =6
            user_id =2
        ####################
        return ProductView.as_view()(request, product_id,user_id)