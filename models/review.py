#!/usr/bin/env python3
"""class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review which inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
