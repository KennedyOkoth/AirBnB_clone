#!/usr/bin/python3
"""
This is my base model
takes in public instances attributes id,created_at
and updated at.
"""
import uuid
from datetime import datetime
from models import storage

"""
Parent class to all the classes in AirBnB lone project
"""


class BaseModel:
    """Parent class for AirBnB clone project
    Methods:
            __init__(self, *args, **kwargs)
            __str__(self)
            save(self)
            to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated
        """
        if kwargs:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
                    setattr(self, attr, datetime.fromisoformat(value))
                    continue

                if attr != "__class__":
                    setattr(self, attr, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return class name, id, and the dictionary
        """
        return f"{type(self).__name__} {self.id} {self.__dict__}"

    def save(self):
        """
        Instance method to:
        - update current datetime
        - invoke save() function &
        - save to serialized file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        obj_dict = {**self.__dict__}
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
