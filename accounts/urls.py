from django.urls import path, include
from djoser.views import (
    UserCreateView,
    UserActivateView,
    UserViewSet,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('activate/<str:uid>/<str:token>/', UserActivateView.as_view(), name='activate'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
]
