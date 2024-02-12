#!/usr/bin/python3
'''Defines a Rectangle model that inherits from Base class.'''

from models.base import Base

class Rectangle(Base):
    '''Represent a Rectangle model.

    Attributes:
        __width: The width of the rectangle
        __height: The height of the rectangle
        __x: The x position of the rectangle
        __y: The y position of the rectangle
    '''

    @staticmethod
    def validate_int(value, attribute_name, equal=False):
        '''Validates if the value is an integer and optionally greater than 0.'''
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{attribute_name} must be an integer")
        if equal:
            if value < 0:
                raise ValueError(f"{attribute_name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{attribute_name} must be > 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Construct'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.validate_int(value, "width")
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.validate_int(value, "height")
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.validate_int(value, "x", equal=True)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.validate_int(value, "y", equal=True)
        self.__y = value

    def area(self):
        '''Returns the area value of the rectangle'''
        return self.height * self.width

    def display(self):
        '''Prints the rectangle using the character #'''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args:
            for i, arg in enumerate(args):
                setattr(self, ['id', 'width', 'height', 'x', 'y'][i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Represents a dictionary of Rectangle'''
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
