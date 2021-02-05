from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveView.as_view()),
    path('products/categories', CategoryListView.as_view()),
]
