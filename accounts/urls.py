from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from accounts.views import CustomUserView, CustomUserCreate, CustomConfirmEmailView

urlpatterns = [
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('v1/users/me/', CustomUserView.as_view(), name='user_profile'),
    path('v1/users/', CustomUserCreate.as_view(), name='create_user'),
    path('v1/rest-auth/registration/account-confirm-email/<str:key>/', CustomConfirmEmailView.as_view(),
         name='account_confirm_email'),
    path('v1/token-auth/', obtain_jwt_token),
    path('v1/token-refresh/', refresh_jwt_token),
]