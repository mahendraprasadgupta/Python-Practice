# Generators in Python
# There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.

# This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

# Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# Create Generators in Python
# It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield statement instead of a return statement.

# If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

# The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
print(a)
next(a)
next(a)
next(a)

for x in my_gen():
    print(x)


# String Revers using Genrator

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)