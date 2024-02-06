#!/usr/bin/python3
'''Define a reading text file function.'''


def read_file(filename=""):
    '''Print the content of a UTF-8 text file.'''
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
