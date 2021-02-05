from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('upload', NProductListView.as_view(), name='upload'),
    path('', views.main, name='main'),
    path('livelist',views.livelist, name='livelist'),
    path('post', views.post, name='post'),
    path('view_product', views.view_product,name='view_product'),
    path('category', views.category, name ='category'),
    path('search', views.search, name ='search')
]
