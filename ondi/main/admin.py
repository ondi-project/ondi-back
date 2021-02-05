from django.contrib import admin

from .models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_category','p_name','p_date','p_seller')
    fields =()
# admin.site.register(Product)
@admin.register(LiveProduct)
class LiveProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'l_product', 'l_date', 'l_sprice')
    fields = ()
