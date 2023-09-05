#!/usr/bin/python3 
def text_indentation(text):

    """
        Args:
            text - words of two lines

        Returns: A text

        Raises:
            TypeError: text must be a string
    """
    """checks if text is a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    new_text = ""
    """ Adds character to current line"""
    for i in text:
        new_text += i
    
    """ Check if the character is '.', '?', or ':' """
    if i in '.?:':
        print(new_text.strip())

        """ Reset line """
        new_text =""

        """ prints previous line if not empty"""
    if new_text:
        print(new_text.strip())
