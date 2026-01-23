# Creation: Square brackets
my_list = []                     # Empty list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14] # Lists can hold any type

# Access: Zero-based indexing
first_fruit = fruits[0]          # "apple" (first item is at index 0)
last_fruit = fruits[-1]          # "cherry" (negative index counts from the end)

# Slicing: [start:stop:step] (stop is exclusive)
subset = numbers[1:4]            # [2, 3, 4] (items at index 1, 2, 3)
every_other = numbers[::2]       # [1, 3, 5]
reversed_list = numbers[::-1]    # [5, 4, 3, 2, 1]

# Key Methods (list is mutable - it changes in place)
fruits.append("date")            # Adds to the end: ["apple", "banana", "cherry", "date"]
fruits.insert(1, "blueberry")    # Inserts at index 1
removed_item = fruits.pop()      # Removes & returns last item ("date")
removed_index = fruits.pop(0)    # Removes & returns item at index 0 ("apple")
fruits.sort()                    # Sorts alphabetically (changes the original list)
sorted_fruits = sorted(fruits)   # Returns a new sorted list
fruits.reverse()                 # Reverses the list in place


count_banana = fruits.count("banana")  # Counts occurrences of "banana"
index_of_cherry = fruits.index("cherry")  # Finds index of "cherry"
fruits.remove("banana")         # Removes first occurrence of "banana"
fruits.extend(["elderberry", "fig"])  # Extends list with another list


# `fruits.extend(["elderberry", "fig"])` means:

# ✅ **Add each item** from the given list **into `fruits`**, one by one.

# So it **expands** the original list.

# ### Example:

# ```python
# fruits = ["apple", "banana"]

# fruits.extend(["elderberry", "fig"])

# print(fruits)
# ```

# ✅ Output:

# ```python
# ['apple', 'banana', 'elderberry', 'fig']
# ```

# ### Important difference:

# #### `extend()` adds items separately

# ```python
# fruits.extend(["x", "y"])
# # becomes ... 'x', 'y'
# ```

# #### `append()` adds the whole list as ONE item

# ```python
# fruits.append(["x", "y"])
# # becomes ... ['x', 'y'] as a single element
# ```

length = len(fruits)            # Number of items in the list
clear_list = fruits.clear()     # Empties the list

# List Comprehensions: concise way to create lists
