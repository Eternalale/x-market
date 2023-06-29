from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_auth.registration.views import VerifyEmailView


class EmailVerificationView(VerifyEmailView):
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.confirm(self.request)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
