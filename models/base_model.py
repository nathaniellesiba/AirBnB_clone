#!/usr/bin/python3
"""the module defines a base class for all models"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes and methods for other classes"""

    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(cls,self.id, self.__dict__)

    def save(self):
        """Update public instance attr updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary containing all keys/values
        of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
