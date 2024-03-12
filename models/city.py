#!/usr/bin/python3
""" City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class, contains state ID and name """
    state_id = ""
    name = ""
