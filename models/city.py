#!/usr/bin/env python3
"""class City which inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class city which has state_id and name
    """
    state_id = ""
    name = ""
