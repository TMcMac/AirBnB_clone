#!/usr/bin/env python3
'''Unittest for Amenity'''
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(TestCase):
    '''Tests Amenity class'''
    def test_init(self):
        obj = Amenity()
        self.assertIsInstance(obj, BaseModel)
        self.assertIs(type(obj), Amenity)

    def test_name(self):
        amenity = Amenity()
        self.assertIs(amenity.name, '')
