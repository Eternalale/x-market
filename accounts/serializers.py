from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from django.conf import settings
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return '{}/{}'.format(
            settings.REST_AUTH_REGISTER_VERIFICATION_URL, emailconfirmation.key
        )


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Неверный email или пароль")
        else:
            raise serializers.ValidationError("Email и пароль обязательны")

        data['user'] = user
        return data
    