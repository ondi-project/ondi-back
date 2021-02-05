from rest_framework import serializers
from .models import *
from user.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'seller', 'view_count']

    liked = serializers.SerializerMethodField()
    def get_liked(self, obj):
        request = self.context.get('request', None)
        if request:
            user = request.user
            try:
                like = Like.objects.get(from_user=user, product=obj)
                return True
            except Like.DoesNotExist:
                return False
        return False

    like_count = serializers.SerializerMethodField()
    def get_like_count(self, obj):
        return Like.objects.filter(product=obj).count()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['name']
