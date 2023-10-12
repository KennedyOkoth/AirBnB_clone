#!/usr/bin/python3
"""
AirBnB clone project File Storage
"""
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
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                new_dict_obj = json.load(file)
            for key, value in new_dict_obj.items():
                obj = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
