from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('livelist',views.livelist, name='livelist'),
    path('post', views.post, name='post'),
    path('view_product', views.view_product,name='view_product'),
    path('category', views.category, name ='category'),
    path('search', views.search, name ='search')
]
