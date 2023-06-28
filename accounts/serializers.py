from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'first_name', 'last_name')
