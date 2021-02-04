from django.db import models

# Create your models here.
class Product(models.Model):
    #상품 DB {카테고리 / 이름/가격/내용/사진/협상여부/태그/등록시간}
    p_category = models.CharField(max_length=200)
    p_name = models.CharField(max_length=200)
    p_price = models.CharField(max_length=200)
    p_content = models.CharField(max_length=200)
    #p_photo
    p_nego=models.CharField(max_length=200)
    p_tag=models.CharField(max_length=200)
    p_date = models.DateTimeField('date published')