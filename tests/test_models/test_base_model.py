#!/usr/bin/python3
'''Unit tests for BaseModel'''
from unittest import TestCase
from models.base_model import BaseModel

class TestBaseModel(TestCase):
    '''Tests BaseModel'''
    def test_init(self):
        '''tests init'''
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIn('id', base.__dict__)
        self.assertIn('created_at', base.__dict__)
        self.assertIn('updated_at', base.__dict__)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertisInstance(base.updated_at, datetime)
