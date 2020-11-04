#!/usr/bin/env python3
'''Unittest for User'''
from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    '''Tests User class'''
    def test_init(self):
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIs(type(user), User)

    def test_first_name(self):
        user = User()
        self.assertIs(user.first_name, '')
