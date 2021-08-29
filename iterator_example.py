# Iterators in Python
# Difficulty Level : Easy

# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

# Example

str1 = "Mahendra Gupta"
res = iter(str1)

while True:
 
 try:
 
        # Iterate by calling next
        item = next(res)
        print(item)
 except StopIteration:
 
        # exception will happen when iteration will over
        break
