#!/usr/bin/python3
'''Defines a Base model class.'''

import json
import csv

class Base():
    '''Represent a base model.

    Attributes:
       __nb_objects: The number of instantiated bases.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Construct

        Args:
           id: The identity of a new base.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Represents  list_dictionaries in a JSON string'''
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w', encoding="utf-8") as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''Represents json_string as a list'''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances.'''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as myfile:
                list_dict = cls.from_json_string(myfile.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the csv serializtion of a list of objects'''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="utf-8") as myfile:
            if list_objs is None or list_objs == []:
                myfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(myfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instantiated fro a csv file.'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []