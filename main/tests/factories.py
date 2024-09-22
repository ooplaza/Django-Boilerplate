import factory
from main.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """
    User factory.
    """

    class Meta:
        model = User

    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    contact_number = factory.Faker("phone_number")
    password = factory.Faker("password")

    @classmethod
    def create_superuser(cls, **kwargs):
        """
        Create a superuser.
        """
        return cls(is_superuser=True, **kwargs)
