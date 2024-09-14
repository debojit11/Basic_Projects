# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(sequence, start=0):
    """
    Custom implementation of the built-in enumerate() function.

    Args:
        sequence (iterable): The input sequence (list, tuple, etc.) to enumerate over.
        start (int): The starting index for enumeration. Defaults to 0.

    Returns:
        list: A list of tuples where each tuple contains an index and the corresponding item from the sequence.
    """
    result = []
    index = start
    for item in sequence:
        result.append((index, item))
        index += 1
    return result

# Example list of courses
courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

# Using the custom my_enumerate function
for index, course in my_enumerate(courses):
    print(f"{index}: {course} Python")
