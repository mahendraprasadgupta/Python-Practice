# Decorators 
# Decorators are very powerful and useful tool in Python since it allows programmers to modify
# the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
# without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.


# 1. type decorator
#====================================

# defining a decorator
def hello_decorator(func):
  
    # inner1 is a Wrapper function in 
    # which the argument is called
      
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
  
        # calling the actual function now
        # inside the wrapper function.
        func()
  
        print("This is after function execution")
          
    return inner1
  
  
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")
  
  
# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)
  
  
# calling the function
function_to_be_used()

# 2. Type Decorator
#=============================

# importing libraries
import time
import math
  
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
      
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
  
        # storing time before function execution
        begin = time.time()
          
        func(*args, **kwargs)
  
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
  
    return inner1
  
  
  
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
  
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
  
# calling the function.
factorial(10)

