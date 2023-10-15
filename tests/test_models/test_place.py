#!/usr/bin/python3
"""This test module defines tests for place.py"""

import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """tests for class Place"""

    def setUp(self):
        """setup Place"""
        self.place = Place()

    def test_attribute_initialization(self):
        """test if attributes initialize"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """test if the attributes are the correct type"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attribute_values(self):
        """test values setting"""
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Example Place"
        self.place.description = "This is a test place"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["wifi", "parking"]

        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Example Place")
        self.assertEqual(self.place.description, "This is a test place")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["wifi", "parking"])

    def test_update_attribute_values(self):
        """test if values can be updated"""
        self.place.name = "Updated Name"
        self.place.number_rooms = 3
        self.place.price_by_night = 150

        self.assertEqual(self.place.name, "Updated Name")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.price_by_night, 150)

    def test_boundary_conditions(self):
        """the the boundaries of conditions"""
        self.place.number_rooms = 1000000
        self.place.price_by_night = 9999999999
        self.place.latitude = 90.0
        self.place.longitude = 180.0

        self.assertEqual(self.place.number_rooms, 1000000)


if __name__ == "__main__":
    unittest.main()
