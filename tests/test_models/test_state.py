#!/usr/bin/python3
"""This test module defines tests for amenity.py"""

import unittest
from models.state import State
from models import storage


class TestAmenity(unittest.TestCase):
    """test for the amenity class"""

    def setUp(self):
        """set up the class"""
        self.state = State()

    def test_attribute_initialization(self):
        """test if class initializes"""
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        """test if attribute name is a string"""
        self.assertIsInstance(self.state.name, str)

    def test_attribute_values(self):
        """test if the values are set correctly"""
        self.state.name = "Abuja"

        self.assertEqual(self.state.name, "Abuja")

    def test_update_attribute_values(self):
        """test if values update correctly"""
        self.state.name = "Nairobi"

        self.assertEqual(self.state.name, "Nairobi")


if __name__ == "__main__":
    unittest.main()
