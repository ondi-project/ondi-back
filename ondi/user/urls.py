from django.urls import path

from .views import *

urlpatterns = [
    path('', UserListCreate.as_view()),
]
