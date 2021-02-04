from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserListView.as_view()),
    path('reports', ReportListCreateView.as_view()),
]
