import re

from rest_framework import serializers


def password_validator(value):
    """Validate password to ensure it meets requirements."""
    if not re.search(r"[a-z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one lowercase letter."
        )
    if not re.search(r"[A-Z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one uppercase letter."
        )
    if not re.search(r"\d", value):
        raise serializers.ValidationError("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&_*()]", value):
        raise serializers.ValidationError(
            "Password must contain at least one special character (!@#$%^&_*())."
        )
