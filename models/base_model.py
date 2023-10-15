#!/usr/bin/python3
"""
This is my base model
takes in public instances attributes id,created_at
and updated at.
"""
import uuid
from datetime import datetime
import models

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
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat
                setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

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
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        obj_dict = {**self.__dict__}
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
