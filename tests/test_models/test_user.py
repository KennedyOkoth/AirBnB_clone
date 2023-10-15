#!/usr/bin/python3
"""This test module defines tests for user.py"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """test user class"""

    def setUp(self):
        """set up User class"""
        self.user = User()

    def test_initialize(self):
        """initialize User class"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attributes(self):
        """test attribute setup"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_creation(self):
        """set values for attributes"""
        user = User(
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """set dictionary for user"""
        user = User(
            email="test@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_user_from_dict(self):
        """collect data from dict"""
        user_data = {
            "__class__": "User",
            "id": "123",
            "email": "test@example.com",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe",
        }
        user = User(**user_data)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
