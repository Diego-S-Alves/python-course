"""Python any() function
The any() function returns True if any item in an iterable are true, otherwise it returns False. However, if the iterable object is empty, the any () function will return False.

Syntax
any(iterable)
The iterable object can be a list, tuple or dictionary.

Example 1
>>> mylst = [ False, True, False]
>>> x = any(mylst)
>>> x
True
Output

Output is True because the second item is True.
Example 2
Tuple – check if any item is True

>>> #Tuple - check if any item is True
>>> mytuple = (0, 1, 0, False)
>>> x = any(mytuple)
>>> print(x)
True
Example 3
Set – Check if any item is True

>>> myset = {0, 1, 0 }
>>> x = any(myset)
>>> print(x)
True
Example 4
Dictionary – check if any item is true in dictionary

>>> mydict = { 0 : "Apple", 1: "Banana"}
>>> x = any(mydict)
>>> print(x)
True
Return Value from any()
any() returns:

True – if atleast one item of the iterable is True.

False – if all the items are False or if an iterable is empty.

When
Return Value
All values are true
True
At least one value is True
True
All values are false
False
Empty iterable
False
Python all() function
The all() function returns True if all items in an iterable are true, otherwise it returns False. If the iterable object is empty, the all() function all returns True.

Syntax
all(iterable)
The iterable object can be list, tuple or dictionary.

Example1 List- Check if all items are True

>>> mylst = [True, True, False]
>>> x = all(mylst)
>>> print(x)
False
Above result shows False, as one of the item in the list is False.

Example 2 Tuple – Check if all items are True in tuple

>>> mytuple = (0, True, False)
>>> x = all(mytuple)
>>> print(x)
False
Example 3: Set – check if all items are True in Set.

>>> myset = {True, 1, 1}
>>> x = all(myset)
>>> print(x)
True
Example 4: Dictionary – check if all item are true in dictionary

>>> mydict = {0: "Apple", 1:"Banana"}
>>> x = all(mydict)
>>> print(x)
False
Return value from all()
The all() method returns

True – if all elements in an iterable are true

False – if any element in an iterable is false

When
Return Value
All values are true
True
At least one value is True
True
All values are false
False
Empty iterable
False"""