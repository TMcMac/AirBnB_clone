#!/usr/bin/env python3
"""The basemodel for all other object"""
from datetime import datetime
import uuid


class BaseModel():
    """
    This is the basemodel from which all other
    objects in our project will inherit an id
    and certain methods
    """

    def __init__(self):
        """
        Initialization method for a BaseModel Object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        """
        Prints the String Rep of an object
        """
        name = (self.__class__.__name__)
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """
        Saves the representation of the object to a dict
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dict of the object
        """
        eggplant = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            if k == 'created_at':
                new_key = 'created_at'
                new_value = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
                eggplant.update({new_key: new_value})
            elif k == 'updated_at':
                new_key = 'updated_at'
                new_value = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
                eggplant.update({new_key: new_value})
            else:
                eggplant.update({k: v})
        return (eggplant)
