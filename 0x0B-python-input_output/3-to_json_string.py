#!/usr/bin/python3
'''Define a string-to-JSON function.'''
import json


def to_json_string(my_obj):
    '''Return the JSON representation for a string object.'''
    return (json.dumps(my_obj))
