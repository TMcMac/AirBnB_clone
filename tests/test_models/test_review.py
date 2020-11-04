#!/usr/bin/env python3
'''Unittest for review'''
from unittest import TestCase
from models.review import Review


class TestReview(TestCase):
    '''Tests Review class'''
    def test_init(self):
        obj = Review()
        self.assertIsInstance(obj, BaseModel)
        self.assertIs(type(obj), Review)

    def test_text(self):
        obj = Review()
        self.assertIs(obj.text, '')
