from main.models import User
from rest_framework import serializers
from abstract.serializers import AbstractSerializer


class UserSerializer(serializers.ModelSerializer, AbstractSerializer):
    """
    User serializer.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "is_active",
            "created_at",
            "updated_at",
            "contact_number",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "is_active": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
        }
