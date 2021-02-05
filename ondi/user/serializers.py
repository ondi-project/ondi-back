from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
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
            'image',
        ]

class UserRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=11)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone = self.data.get('phone')
        user.save()
        return user

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'to_user',
            'message',
        ]

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'id',
            'from_user',
            'to_user',
            'content',
        ]
        read_only_fields = ['from_user',]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score 
        fields = [
            'id',
            'from_user',
            'to_user',
            'score',
            'comment',
        ]
        read_only_fields = ['from_user',]
