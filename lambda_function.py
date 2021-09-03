# Lambda functions

# A Lambda Function is a small, anonymous function — anonymous in the sense that it doesn’t actually have a name.
# Python functions are typically defined using the style of def a_function_name() , but with lambda functions we don’t give it a name at all. We do this because the purpose of a lambda function is to perform some kind of simple expression or operation without the need for fully defining a function.
# A lambda function can take any number of arguments, but must always have only one expression:

x = lambda a, b : a * b
print(x(5, 6)) # prints '30'

x = lambda a : a*3 + 3
print(x(3)) # prints '12'


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you hav
