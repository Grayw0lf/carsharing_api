from rest_framework import serializers
from rest_framework.authentication import authenticate
from .models import CarShareUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):
        return CarShareUser.objects.create_user(**validated_data)

    class Meta:
        model = CarShareUser
        fields = ('email', 'username', 'password', 'token')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {'token': user.token,}


class CarShareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShareUser
        fields = ('email', 'username', 'user_lang')
