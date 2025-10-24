# create complex numbers
a = 3 + 4j
b = complex(1, -2)
c = 0.5 + 0j  # complex with zero imaginary part
print()
# store them in a list
z_list = [a, b, c]
print(z_list)               # [(3+4j), (1-2j), (0.5+0j)]

# index, iterate
print(z_list[0])            # (3+4j)
for z in z_list:
    print(z.real, z.imag)   # access real and imaginary parts
print()
# arithmetic
total = sum(z_list)         # (4.5+2j)
print(total)
print()
# list operations
z_list.append(2+3j)
z_list[1] = complex(2, 2)
print()
# list -------------------------------------------------------------------
z_list = [3+4j, 1-2j, 0.5+0j]  # example of list with complex numbers
print("first:", z_list[0])
print("sum:", sum(z_list))
print("sorted by magnitude:", sorted(z_list, key=abs))
#a tuple--------------------------------------------------------------------
t1 = (1, 2, 3)  # this is a tuple
t2 = (1, "two", 3.0)
t3 = 3, 4, 5         # parentheses optional (packing)
t_single = (42,)     # single-item tuple needs a trailing comma
empty = ()           # empty tuple
print()
# dictionary--------------------------------------------------------------------
# literal    this is a dictionary
d = {"name": "Alice", "age": 25}

# from pairs
d2 = dict([("x", 1), ("y", 2)])

# with keyword args
d3 = dict(city="Paris", country="France")
print(d3["city"])
# empty
empty = {}
# set--------------------------------------------------------------------
print()
s1 = {1, 2, 3}        # literal   this is a set
s2 = set([1, 2, 2, 3])# from iterable -> {1,2,3}
empty = set()         # empty set (not {} — that's an empty dict)
fs = frozenset([1,2]) # immutable set