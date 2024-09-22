from main.models import User
from rest_framework.test import APITestCase


class UserModelAndManagerTestCase(APITestCase):
    """
    Test the user model and manager.
    """

    @classmethod
    def setUpTestData(cls):
        cls.basic_user = User.objects.create_user(
            email="test@gmail.com",
            password="testpassword",
        )
        cls.super_user = User.objects.create_superuser(
            email="superuser@gmail.com",
            password="superuserpassword",
        )

    def test_create_basic_user(self):
        """
        Test creating a user.
        """
        user = User.objects.get(email=self.basic_user.email)
        self.assertEqual(user.email, self.basic_user.email)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = User.objects.get(email=self.super_user.email)
        self.assertEqual(user.email, self.super_user.email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_with_raises_error(self):
        """
        Test creating a user with no email or password.
        """

        payloads = [
            {
                "email": "",
                "password": "testpassword",
            },
            {
                "email": "basicuser@gmail.com",
                "password": "",
            }
        ]

        for payload in payloads:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    User.objects.create_user(**payload)

    def test_create_superuser_with_raises_error(self):
        """
        Test creating a user with no email or password.
        """

        payloads = [
            {
                "email": "",
                "password": "testpassword",
            },
            {
                "email": "basicuser@gmail.com",
                "password": "",
            }
        ]

        for payload in payloads:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    User.objects.create_superuser(**payload)
