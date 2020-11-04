#!/usr/bin/env python3
'''Unittest for City'''
from unittest import TestCase
from models.city import City


class TestCity(TestCase):
    '''Tests City class'''
    def test_init(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIs(type(city), City)

    def test_name(self):
        city = City()
        self.assertIs(city.name, '')
