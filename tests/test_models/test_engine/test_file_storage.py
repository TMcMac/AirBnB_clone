#!/usr/bin/env python3
'''Unittests for file storage engine'''
from unittest import TestCase
from models import storage
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    '''Tests for FileStorage'''
    def test_all(self):
        model = BaseModel()
        poindexter = storage.all()
        assertIn(model, poindexter.values())

    def test_new(self):
        pass
