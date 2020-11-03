#!/usr/bin/env python3
'''Home file for class Review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''For storing attributes of class Review'''
    place_id = ''
    user_id = ''
    text = ''
