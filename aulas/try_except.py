"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

Example
The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

  Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.

Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
"""
