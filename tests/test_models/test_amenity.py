#!/usr/bin/python3
"""This test module defines tests for amenity.py"""

import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """test amenity class"""

    def setUp(self):
        """setup amenity class"""
        self.amenity = Amenity()

    def test_attribute_initialization(self):
        """initialize amenity attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_attribute_types(self):
        """test attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_attribute_values(self):
        """set attribute values"""
        self.amenity.name = "WiFi"

        self.assertEqual(self.amenity.name, "WiFi")

    def test_update_attribute_values(self):
        """update attribute values"""
        self.amenity.name = "Security"

        self.assertEqual(self.amenity.name, "Security")


if __name__ == "__main__":
    unittest.main()
