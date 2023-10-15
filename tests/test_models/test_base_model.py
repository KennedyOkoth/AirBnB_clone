#!/usr/bin/python3
"""This test module defines tests for base_model.py"""

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the model BaseModel"""

    def test_save(self):
        """Confirm save method works"""

        model = BaseModel()
        model.save()

    def test_save_updates_updated_at(self):
        """Confirm that the attribute updated_at is updated when the method
        save is called"""

        model = BaseModel()

        # save the model to file
        model.save()

        # Get the updated_at attribute
        updated_at = model.updated_at

        # Check that updated_at has been updated
        self.assertNotEqual(model.created_at, updated_at)

    def test_to_dict_contains_all_attributes(self):
        """confirm dictionary contains all expected keys"""

        # Create an instance of BaseModel
        model = BaseModel()

        # Convert the model to a dictionary
        model_dict = model.to_dict()

        # Check that the dictionary contains all expected keys
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_to_dict_datetime_formatting(self):
        """confirm created_at and updated_at are strings"""

        # """Create an instance of BaseModel"""
        model = BaseModel()

        # """Convert the model to a dictionary"""
        model_dict = model.to_dict()

        # Check that created_at and updated_at are moved from iSO format to strings
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_id(self):
        """Confirm model ids are unique and the correct type (strings)"""

        # Create two BaseModel instances
        model1 = BaseModel()
        model2 = BaseModel()

        # Test that their ids are unique
        self.assertNotEqual(model1.id, model2.id)

        # Test that their ids are of the correct type
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)

    def test_recreate_instance_from_dictionary(self):
        """Test the recreation of instances using values from a dictionary"""

        # create first instance of BaseModel
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        # create second instance of BaseModel using json
        my_new_model = BaseModel(**my_model_json)

        # test equality of attribute values
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

    def test_save_objects_to_file(self):
        """Tests whether FileStorage can save JSON to a file"""

        # create new model
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
