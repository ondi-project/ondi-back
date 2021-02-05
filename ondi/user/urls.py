from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserListView.as_view()),
    path('reports', ReportListCreateView.as_view()),
    path('reports/<int:pk>', ReportRetrieveDestroyView.as_view()),
    path('notifications', NotificationListCreateView.as_view()),
    path('notifications/<int:pk>', NotificationRetrieveDestroyView.as_view()),
    path('scores', ScoreListCreateView.as_view()),
    path('scores/<int:pk>', ScoreRetrieveDestroyView.as_view()),
]
