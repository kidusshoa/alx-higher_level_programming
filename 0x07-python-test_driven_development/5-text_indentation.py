#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    lines = text.split('\n')

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces
        if line:
            for char in punctuation:
                line = line.replace(char, char + '\n\n')
            print(line)
