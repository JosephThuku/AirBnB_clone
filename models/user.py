#!/usr/bin/env python3
"""class user which inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user with emil,password, first_name and last_name
    """
    email = ''
    password = ''
    first_name = ""
    last_name = ""
