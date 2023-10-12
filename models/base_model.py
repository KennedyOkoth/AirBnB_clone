#!/usr/bin/python3
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
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = self.created_at
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
        obj_dict = self.__dict__
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at
        obj_dict["updated_at"] = self.updated_at
        return obj_dict
