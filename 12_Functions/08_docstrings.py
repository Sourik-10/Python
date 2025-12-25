#Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute.

def add1(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add1.__doc__)  # Output: Returns the sum of two numbers.
 
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b
print(add(2,5))