'''def add(a,b):
 return a+b
result = add(3,3)
print(result)
'''
'''#without return 
def add(a,b):
 print(a+b)
result = add(3,3)
print(result)
'''
#return is more important for using in another function or method

### function can be called from one file to another by usning function name
from test import add
result = add(35,35)
print(result)