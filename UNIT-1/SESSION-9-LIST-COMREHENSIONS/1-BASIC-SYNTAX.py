list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #this is simple list of numbers
print()
print("This is square of even numbers from list1: ", [n**2 for n in list1 if n%2==0])  #this will print square of even numbers from list1
print()
print("This is cube of odd numbers from list1: ", [n**3 for n in list1 if n%2!=0])  #this will print cube of odd numbers from list1
print()
print("This is double of all numbers from list1: ", [n*2 for n in list1])         #this will print double of all numbers from list1