#!/usr/bin/python3

"""Define a model class called Base"""

import json
import turtle
import csv


class Base:
    """This class represents a model.

    It will be the "bases" of other classes in this project.

    Attributes:
        __nb_objects (int): is the number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This method initialize a new base.

        Args:
            id (int): is the identity of the new base.
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance
