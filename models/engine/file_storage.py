#!/usr/bin/python3
"""
AirBnB clone project File Storage
"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """This is a storage engine for AirBnB clone project
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Serializes, or converts Python objects into JSON strings
        reload: Deserializes, or converts JSON strings into Python objects.
    Class Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        class_dict (dict): A dictionary of all the classes.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            json.dump({k: v.to_dict()
                       for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        class_dict = {"BaseModel": BaseModel}
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: class_dict[k.split(".")[0]](**v)
                for k, v in deserialized.items()
            }
