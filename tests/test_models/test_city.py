#!/usr/bin/python3
"""This test module defines tests for city.py"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test cases for the city class"""

    def setUp(self):
        """setup city"""
        self.city = City()

    def test_attribute_initialization(self):
        """test if attribute are set correctly"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attribute_types(self):
        """test for correct attribut types"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_attribute_values(self):
        """set values for attributes"""
        self.city.state_id = "123"
        self.city.name = "Nairobi"

        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "Nairobi")

    def test_update_attribute_values(self):
        """update values of city"""
        self.city.name = "Mombasa"

        self.assertEqual(self.city.name, "Mombasa")


if __name__ == "__main__":
    unittest.main()
