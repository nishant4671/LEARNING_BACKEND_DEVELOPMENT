# Creation: Curly braces without colons (or set() constructor)
my_set = set()                   # Empty set (NOT {}, that's an empty dict)
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}

# Key Property: Automatically enforces uniqueness
numbers_with_dupes = [1, 2, 2, 3, 3, 3]
unique_set = set(numbers_with_dupes)  # {1, 2, 3} (duplicates removed)

# Adding/Removing
unique_numbers.add(6)            # {1, 2, 3, 4, 5, 6}
unique_numbers.remove(3)         # {1, 2, 4, 5, 6} (raises error if item not found)
unique_numbers.discard(10)       # {1, 2, 4, 5, 6} (no error if item not found)

# Set Operations (Mathematical)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b            # {1, 2, 3, 4, 5, 6} (all items in either)
intersection = set_a & set_b     # {3, 4} (items in both)
difference = set_a - set_b       # {1, 2} (items only in set_a)
symmetric_diff = set_a ^ set_b   # {1, 2, 5, 6} (items in one set but not both)
# Membership Testing
is_in_set = 2 in unique_numbers   # True



