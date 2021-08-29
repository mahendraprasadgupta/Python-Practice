"""
Docstrings in Python are used not only for the description of a class or a function to provide a better understanding of the code and use but, also used for Testing purposes.

The Doctest Module finds patterns in the docstring that looks like interactive shell commands.

The input and expected output are included in the docstring, then the doctest module uses this docstring for testing the processed output.
After parsing through the docstring, the parsed text is executed as python shell commands and the result is compared with the expected outcome fetched from the docstring.
"""

# import testmod for testing our function
from doctest import testmod
  
# define a function to test
def factorial(n):
    '''
    This function calculates recursively and
    returns the factorial of a positive number.
    Define input and expected output:
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)
  
# call the testmod function
if __name__ == '__main__':
    testmod(name ='factorial', verbose = True)