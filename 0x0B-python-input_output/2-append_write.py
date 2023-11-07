#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8) and \
        returns the number of characters added."""


def append_write(filename="", text=""):
    """
    Appends the given text to a file in UTF-8 encoding and returns the \
            number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            # Append the text to the file
            num_characters_added = file.write(text)
            return num_characters_added

    except Exception as e:
        # Handle exceptions if any
        return (0)

