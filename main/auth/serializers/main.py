from typing import Any, Dict
from main.models import User
from django.db import transaction
from rest_framework import serializers
from main.serializers import UserSerializer
from main.utils.validator import password_validator
from rest_framework_simplejwt.tokens import TokenError
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings
from dj_rest_auth.jwt_auth import CookieTokenRefreshSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken



class RegisterSerializer(UserSerializer):
    """
    Register serializer.
    """

    password = serializers.CharField(
        min_length=8,
        required=True,
        write_only=True,
        max_length=255,
        style={"input_type": "password"},
        error_messages={
            "blank": "This field is required",
            "null": "This field is required.",
        }
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "last_name",
            "first_name",
            "contact_number",
        ]
        extra_fields = {
            "id": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def validate_password(self, value):
        """Validate password to ensure it meets requirements."""
        password_validator(value)
        return value

    def create(self, validated_data):
        """
        Modify the create method to hash the password.
        """

        with transaction.atomic():
            password = validated_data.pop("password")
            User.objects.create_user(password=password, **validated_data)
            return validated_data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Login Serializer."""
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
        Validate the credentials
        """
        if "email" in attrs:
            attrs["email"] = attrs["email"].lower()

        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data

        # Update last timestamp of the user
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class CustomCookieTokenRefreshSerializer(CookieTokenRefreshSerializer):
    """Refresh Token Serializer."""
    is_http_cookie_only = serializers.BooleanField(required=False)

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
        Validate the refresh token.
        """
        try:
            data = super().validate(attrs)
            return data
        except TokenError as error:
            raise serializers.ValidationError(
                {
                    "details": str(error),
                    "code": "token_not_valid"
                }
            )
        except BlacklistedToken as error:
            raise serializers.ValidationError(
                {
                    "details": str(error),
                    "code": "token_blacklisted"
                }
            )
