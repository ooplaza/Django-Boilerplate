from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from main.auth.serializers.main import (
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    CustomCookieTokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class RegisterView(GenericAPIView):
    """
    An endpoint for registering users.
    """

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Register a new user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"details": "Successfully Registered"},
            status=status.HTTP_201_CREATED
        )


class LoginView(GenericAPIView):
    """
    An endpoint for logging in users.
    """

    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """
        Login a user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )


class RefreshTokenView(GenericAPIView):
    """
    An endpoint for refreshing tokens.
    """

    permission_classes = [AllowAny]
    serializer_class = CustomCookieTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        """
        Refresh a token.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "Token refreshed successfully",
                **serializer.validated_data
            },
            status=status.HTTP_200_OK
        )


class LogoutView(GenericAPIView):
    """
    An endpoint for logging out users.
    """

    permission_classes = [AllowAny]
    serializer_class = CustomCookieTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        """Logout a user."""
        refresh_token = request.data.get("refresh", None)

        if not refresh_token:
            return Response(
                {"details": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError as error:
            return Response(
                {"details": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

        response = Response(
            {"message": "Logout Successful"},
            status=status.HTTP_200_OK
        )

        response.delete_cookie("refresh")
        response.delete_cookie("access")
        return response
