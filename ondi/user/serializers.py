from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
            'phone',
        ]

class UserRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=11)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone = self.data.get('phone')
        user.save()
        return user
