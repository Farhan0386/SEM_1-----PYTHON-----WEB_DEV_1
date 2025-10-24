# Docstring comments: Python docstring is the string literals with triple quotes
def add(a ,b):
       """Function to add the value of a and b """
       return a+b
       print(add.__doc__)   # this is method to use python docstring  comments.
print()
       
# this is multi line statement using backslash (\) . this is known as explicit line continuation
total=12 + \
      13 + \
      33
print(total)
print()
# this is multi line statement using parentheses . this is known as implicit line continuation
total2=(12 + 
        13 + 
        33)
print(total2)
print()
# Note: we can use multi line statement in list, dictionary, tuple, set etc.

# this is multi line statement using triple quotes
total3 = """12 +
            13 +
            33"""
print(total3)
print()

# this is a built in module used for list of keywords in python which is known as keyword module
import keyword
print("List of keywords in python are:")
print(keyword.kwlist)
print()