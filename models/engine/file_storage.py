#!/usr/bin/env python3
'''
serializes instances to a JSON file and deserializes JSON file to instances
'''

import json
import os


class FileStorage:
    '''serializes instances to a JSON file
    and deserializes JSON file to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns dictionary of objects'''
        return self.__objects

    def new(self, obj):
        '''creates new object entry'''
        key = str(obj.__class__.__name__ + '.' + obj.id)
        return self.__objects.update({key: obj})

    def save(self):
        '''saves all objects to JSON file'''
        with open(self.__file_path, 'w') as f:
            poindexter = {}
            for key, value in self.__objects.items():
                poindexter.update({key: value.to_dict()})
            json.dump(poindexter, f)

    def reload(self):
        '''loads objects from JSON file'''
        try:
            with open(self.__file_path) as f:
                undead = json.load(f)
                for key, value in undead:
                    obj_class = value['__class__']
                    new_zombie = obj_class(**value)
                    self.new(new_zombie)
        except:
            pass
