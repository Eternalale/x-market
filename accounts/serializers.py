from rest_framework import serializers
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer

from accounts.models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'first_name', 'last_name',)
        read_only_fields = ('email',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'first_name', 'last_name',)
        read_only_fields = ('email',)
