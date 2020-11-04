#!/usr/bin/env python3
'''Unittest for place'''
from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    '''Tests Place class'''
    def test_init(self):
        obj = Place()
        self.assertIsInstance(obj, BaseModel)
        self.assertIs(type(obj), Place)

    def test_name(self):
        obj = Place()
        self.assertIs(obj.name, '')
