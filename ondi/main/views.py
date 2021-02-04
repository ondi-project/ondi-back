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

#Main화면 : 상품들 최신순으로 보여짐
@method_decorator(csrf_exempt,name='dispatch')
def main(request):
    if request.method == "GET":
        return ProductListView.as_view()(request)