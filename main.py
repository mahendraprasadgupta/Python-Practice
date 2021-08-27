import docString as obj #import everything in obj from docString
from docString import __version__ #import __version__ only from docString
import docString #import docString directly 
import sys 

print(docString.testfunc)

obj1=obj.Test()
print(obj1.testfunc1.__doc__)


print(obj.testfunc())
print(obj.__version__)
print(obj.testfunc.__doc__)
print(obj.func.__annotations__)
print(obj.__dict__)


print(sys.path)
print(dir())
print(__name__)


