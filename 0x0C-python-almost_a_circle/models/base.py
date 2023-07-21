#!/usr/bin/python3
"""Defines a class Base"""

import json


class Base:
    """Base class
    Args:
        __nb_objects (int): private num objects attr
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor, initilise new obj
        Args:
            id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """List of dictionaries to JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string rep of list obj to file"""
        list_dicts = []

        filename = "{}.json".format(cls.__name__)

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                for i in range(list_objs):
                    list_dicts.append(list_objs[i].to_dictionary())
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns json string rep of list of dictionaries"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instance(object) from dictionary of attributes"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances(objects) from file"""
        list_instances = []

        filename = "{}.json".format(cls.__name__)

        with open(filename, "r") as file:
            if not filename:
                return "[]"
            else:
                list_dicts = cls.from_json_string(file.read())
                for i in range(list_dicts):
                    list_instances.append(cls.create(**list_cls[i])) 
