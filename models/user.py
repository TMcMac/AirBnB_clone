#!/usr/bin/env python3
'''Home file for class User'''

from models.base_model import BaseModel


class User(BaseModel):
    '''used for defining attributes of users'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
