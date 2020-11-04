#!/usr/bin/env python3
'''Unittest for State'''
from unittest import TestCase
from models.state import State


class TestState(TestCase):
    '''Tests State class'''
    def test_init(self):
        obj = State()
        self.assertIsInstance(obj, BaseModel)
        self.assertIs(type(obj), State)

    def test_name(self):
        obj = State()
        self.assertIs(obj.name, '')
