#!/usr/bin/python3
"""
This is my base model
takes in public instances attributes id,created_at
and updated at.
"""
import uuid
from datetime import datetime
from models import storage


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
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "id":
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Return class name, id, and the dictionary
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

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
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
