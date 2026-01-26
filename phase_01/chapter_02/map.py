# map(function, iterable): Applies the function to every item in the iterable (like a list) and returns a map object (which you can convert to a list).

# filter(function, iterable): Applies the function to every item in the iterable and returns a filter object containing only the items for which the function returned True




numbers = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8]




# same thing done using a loop 
doubled = []
for x in numbers:
    doubled.append(x * 2)
print(doubled)
