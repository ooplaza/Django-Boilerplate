from django.db import models
from abstract.models import AbstractModel
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.models import (
    BaseUserManager,
)



class UserManager(BaseUserManager):
    """Custom user manager."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user."""
        if not email:
            raise ValueError("User must have an email address")
        elif not password:
            raise ValueError("User must have a password")

        # Normalize the email address
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        if not email:
            raise ValueError("Superuser must have an email address")
        elif not password:
            raise ValueError("Superuser must have a password")

        superuser = self.create_user(email, password, **extra_fields)
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, AbstractModel, PermissionsMixin):
    """
    Oerride the default user model.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)

    # User Manager
    objects = UserManager()

    # This will be the default field for authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self) -> bool:
        """Return if the user is staff."""
        return self.is_superuser

    def __str__(self) -> str:
        """Return string representation of the User Model."""
        return self.email

    @property
    def full_name(self) -> str:
        """Return the full name of the user."""
        return f"{self.first_name} {self.last_name}"
