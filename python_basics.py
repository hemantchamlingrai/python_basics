# Correct Syntax 
if 5 > 0:
    print("% is bigger.")


# Syntax Error
if 5 >  0:
print("5 is bigger.")


# Single line Comment


"""Multi
line
Comment"""


# Variables
fruit = "Apple"
price = "$20"


# variable can change its type even after declaring
x = 20
x = "Belly"


# Casting: if you want to specify the type of a variable Casting can be helpful
X = str(5)
y = int(2)
z = float(10)

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



# if you want to find the type of a data use type( variable ) function
print(type(x))


# Single quote string ^ double quote string
x = "John"
x = 'John'


# Quotes inside Quotes You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# multiple strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# String Are Arrays
"""Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])
"""

# looping through a string
"""
Since strings are arrays, we can loop through the characters in a string, with a for loop.

Loop through the letters in the word "banana":
for x in "banana":
    print(x)
    """
    
    
# String Length
"""
To get the length of a string, use the len() function.
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
"""

# Check String
""" 
To check if a certain phrase or character is present in a string, we can use the keyword in.

Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

Use it in an if statement:

Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)


Use it in an if statement:

Example
print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
"""




# Assigning multiple values in multiple variables
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = 10, 20, 30


# One Value to Multiple variables
x = y = z = "Orange"



# Unpack a Collection 
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = [10,20,30]
x,y,z = fruits



# Global Variables can be accessed by anyone inside and outside of a function
greeting = "Hello, World"

def greet():
    print(greeting)

greet()

# if you create the variable with same name in function what will happen? it will be local but if you want to make it global just use global keyword in the function eg: 
# global greeting
greeting = "Hello, World"

def greet():
    greeting = "Hello, Python"
    print(greeting) # This is a local Variable

greet()

print(greeting) # This is a global Variable




# Variable names are Case Sensitive. meaning that 
age = 10
# and 
Age = 30
# and
AGE = 40

# they are different.
# not because of their values its because of their names.

# If variable names contain multiple names then these techniques come in handy

# Camel Case Each word, except the first, starts with a capital letter:
myCarName = "Ford"

# Pascal Case Each word starts with a capital letter:
MyCarName = "Ford"

# Snake Case Each word is separated by an underscore character:
my_car_name = "Ford"




# Built-in Data Types 
"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""



# Setting the data type

"""
Data Type

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	
"""




""" 
Numeric types

int:
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 10
y = 35656222554887711
z = -3255522

float:
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
y = 10.0 
x = 1.10
y = 1.0
z = -35.59

Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100


complex:
Complex numbers are written with a "j" as the imaginary part:
z = ij 
x = 3+5j
y = 5j
z = -5j

"""



# Type Conversion 
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

# Note: You cannot convert complex numbers into another number type.


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random

print(random.randrange(1, 10))