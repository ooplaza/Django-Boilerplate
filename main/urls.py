from django.urls import path
from rest_framework import routers
from main.auth.views.main import (
    LoginView,
    LogoutView,
    RegisterView,
    RefreshTokenView,
)

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("refresh/token", RefreshTokenView.as_view(), name="refresh"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login", LoginView.as_view(), name="login"),
]

urlpatterns += router.urls
