#!/usr/bin/env python3
"""
This is our base model
takes in public instances attributes id,created_at
and updated at.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel describes public instance attributes id,
    created_at and updated at
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method that initializes the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
            else:
                self.id = str(uuid4())
                self.created_at = self.updated_at = datetime.now()
                models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of
        the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
