#!/usr/bin/env python3
"""This test module defines tests for file_storage.py"""

import os
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Instance of FileStorage used in testing"""
        # Create a new instance of FileStorage for each test case
        self.file_storage = FileStorage()

    def test_init(self):
        """check if object is empty and __file_path is set to the correct value"""
        # Test that __objects is an empty dictionary
        self.assertEqual(self.file_storage._FileStorage__objects, {})

        # Test that __file_path is set to the correct default value
        self.assertEqual(self.file_storage._FileStorage__file_path, "file.json")

    def test_all(self):
        """confirm all() works when empty and after objects are added"""
        # Test that all() returns an empty dictionary initially
        self.assertEqual(self.file_storage.all(), {})

        # Add some objects and verify that all() returns the correct dictionary
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        expected_dict = {
            "BaseModel." + obj1.id: obj1.to_dict(),
            "BaseModel." + obj2.id: obj2.to_dict(),
        }
        self.assertEqual(self.file_storage.all(), expected_dict)

    def test_new(self):
        """check that the new method adds to __objects"""
        # Create a test object and add it using the new() method
        obj = BaseModel()
        self.file_storage.new(obj)

        # Verify that the object is added to __objects with the correct key
        expected_key = "BaseModel." + obj.id
        self.assertIn(expected_key, self.file_storage._FileStorage__objects)
        self.assertEqual(
            self.file_storage._FileStorage__objects[expected_key], obj.to_dict()
        )

    def test_save(self):
        """check the save method saves contents to the json file correctly"""
        # Add some objects to __objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Save the objects to the JSON file
        self.file_storage.save()

        # Verify that the JSON file exists
        self.assertTrue(os.path.exists("file.json"))

        # Verify that the contents of the JSON file are correct
        with open("file.json", "r") as f:
            data = json.load(f)
            expected_data = {
                "BaseModel." + obj1.id: obj1.to_dict(),
                "BaseModel." + obj2.id: obj2.to_dict(),
            }
            self.assertEqual(data, expected_data)

    def test_reload(self):
        """check reload method reloads the contents of a json file correctly"""
        # Create a JSON file with some objects
        data = {
            "BaseModel.123": {"id": "123", "name": "object1"},
            "BaseModel.456": {"id": "456", "name": "object2"},
        }
        with open("file.json", "w") as f:
            json.dump(data, f)

        # Reset __objects to an empty dictionary
        self.file_storage._FileStorage__objects = {}

        # Call reload() to load objects from the JSON file
        self.file_storage.reload()

        # Verify that __objects contains the correct objects
        self.assertEqual(self.file_storage._FileStorage__objects, data)


if __name__ == "__main__":
    unittest.main()
