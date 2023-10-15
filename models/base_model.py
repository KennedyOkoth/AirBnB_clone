#!/usr/bin/env python3
"""
This is our base model
takes in public instances attributes id,created_at
and updated at.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel describes public instance attributes id,
    created_at and updated at
    """

    def __init__(self, *args, **kwargs):
        """initialize an instance"""

        if kwargs:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
                    setattr(self, attr, datetime.fromisoformat(value))
                    continue

                if attr != "__class__":
                    setattr(self, attr, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        update the public instance attribute updated_at everytime the object
        is changed
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """create a copy of instance attributes and add class name"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        for attr, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[attr] = value.isoformat()

        return obj_dict
