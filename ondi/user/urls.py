from django.urls import path

from .views import *

urlpatterns = [
    path('users', UserListView.as_view()),
    path('users/<int:pk>', UserRetrieveView.as_view()),
    path('users/<int:pk>/selling', UserSellingListView.as_view()),
    path('users/<int:pk>/sold', UserSoldListView.as_view()),
    path('reports', ReportListCreateView.as_view()),
    path('reports/<int:pk>', ReportRetrieveDestroyView.as_view()),
    path('notifications', NotificationListCreateView.as_view()),
    path('notifications/<int:pk>', NotificationRetrieveDestroyView.as_view()),
    path('scores', ScoreListCreateView.as_view()),
    path('scores/<int:pk>', ScoreRetrieveDestroyView.as_view()),
    path('favorites', FavoriteListCreateView.as_view()),
    path('favorites/<int:pk>', FavoriteRetrieveDestroyView.as_view()),
    path('likes', LikeListCreateView.as_view()),
    path('likes/<int:pk>', LikeRetrieveDestroyView.as_view()),
    path('sold', SoldListCreateView.as_view()),
    path('sold/<int:pk>', SoldRetrieveDestroyView.as_view()),
]
