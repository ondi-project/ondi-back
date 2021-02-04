from django.db import models
from user.models import *
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    #상품 DB
    # {카테고리 / 이름/가격/내용/사진/태그/협상여부/등록시간/좋아요수/판매자}
    p_category = models.CharField(max_length=200)#카테고리선택으로
    p_name = models.CharField(max_length=32, verbose_name="상품제목")
    p_price = models.IntegerField(verbose_name="상품가격", default=0)
    #상품설명 어떻게오느냐따라달라질듯 RichTextUploadingField
    p_content = models.CharField(max_length=32, verbose_name="상품설명")
    p_image = models.ImageField(verbose_name="대표사진", null=True, upload_to="")
    p_tag = models.CharField(max_length=200)
    p_nego = models.BooleanField()
    p_date = models.DateTimeField(default=timezone.now, verbose_name="등록날짜")
    p_likecount = models.IntegerField(verbose_name="좋아요수", null=True, default=0)
    p_seller = models.ForeignKey(User , on_delete=models.CASCADE,default="")
    #라이브방송여부
    p_live = models.CharField(max_length=200, verbose_name="라이브방송여부",default="") #['예정','진행중', '0'] #라이브진행중, 라이브종료,

class LiveProduct(models.Model):
    #일단 상품이아닌 라이브 깜짝방송 이런느낌으로#
    # {상품정보,라이브시간}
    #date확인다시!
    l_date = models.DateTimeField(default=timezone.now, verbose_name="live시작시간")
    l_product = models.ForeignKey(Product, on_delete=models.CASCADE,default="")