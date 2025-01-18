
greeting1 = "Hello World!"
greeting2 = ", trust you're good?"
"""
VOCABULARY
"type" indicates whether a variable is a string, float or integer
"len" indicates the character length of a variable
".isupper()" is like a boolean, identifies through true or false answer prompts if a stringed variable consists of only upper-case letters
".islower()" basically the same as ".isupper", but with lower-case letters
".upper()" is a function that turns all characters of a stringed variable to upper-case letters
".lower()" is basically the same as "upper", but deals in lower-case
"string", is a letter oriented variable
"float" is a decimal number as a variable character
"integer" is a number as a variable character, without a decimal
You can concatenate strings amongst each other, but not with integers and/or floats

In Python, you can print a string and an integer together using several methods. Here is the most prefered one:

Using f-strings (Python 3.6+):

name = "John"
age = 25

print(f"{name} is {age} years old.")
"""
print(greeting1 + greeting2)
print(type(greeting1))
print(len(greeting1))
print(greeting1.isupper())
print(greeting1.islower())
print(greeting1.upper())
print(greeting1.lower())
