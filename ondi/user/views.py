from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from main.serializers import *

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSellingListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
       return Product.objects.filter(p_seller=self.kwargs.get('pk'), p_buy=False)

class UserSoldListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
       return Product.objects.filter(p_seller=self.kwargs.get('pk'), p_buy=True)

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class ReportRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class ScoreRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class FavoriteRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class LikeRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class SoldListCreateView(generics.ListCreateAPIView):
    queryset = Sold.objects.all()
    serializer_class = SoldSerializer
    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

class SoldRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Sold.objects.all()
    serializer_class = SoldSerializer
