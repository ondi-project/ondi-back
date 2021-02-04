from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('livelist',views.livelist, name='livelist'),
    path('post', views.post, name='post'),
    path('view_product', views.view_product,name='view_product'),

]