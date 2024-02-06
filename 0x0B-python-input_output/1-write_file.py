#!/usr/bin/python3
'''Define write a string to a text file function.'''


def write_file(filename="", text=""):
    '''Write a string to the a UTF-8 text file.

    Args:
       filename: The name of the file to write.
       text: The text to write to the file.
    Returns:
       The number of characters written.
    '''
    with open(filename, "w", encoding="utf-8") as myfile:
        return (myfile.write(text))
