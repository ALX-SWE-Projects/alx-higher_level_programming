#!/usr/bin/python3
'''Defines a Square model that inherits from Rectangle class.'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Represent a Square model.

    Attributes:
        __size: The size of the square
        __x: The x position of the square
        __y: The y position of the square
        __id: The id of the square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Construct'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns [Square] (<id>) <x>/<y> - <size>'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args:
            for i, arg in enumerate(args):
                setattr(self, ['id', 'size', 'x', 'y'][i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Represents a dictionary of Square'''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
