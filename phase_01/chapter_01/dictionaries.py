# Creation: Curly braces with key:value pairs
my_dict = {}                     # Empty dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access: Use the key (like an index, but with a label)
name = person["name"]            # "Alice"
age = person.get("age")          # 30 (safer method, returns None if key doesn't exist)

# Adding/Modifying
person["job"] = "Engineer"       # Adds new key-value pair
person["age"] = 31               # Modifies existing value

# Iteration
for key in person:               # Iterates over keys
    print(key)                   # "name", "age", "city", "job"

for key, value in person.items(): # Iterates over key-value pairs
    print(f"{key}: {value}")

# Useful Methods
keys = person.keys()             # dict_keys(['name', 'age', 'city', 'job'])
values = person.values()         # dict_values(['Alice', 31, 'New York', 'Engineer'])
person.pop("city")               # Removes key "city" and returns its value
# Dictionary Basics in Python
# A dictionary is a collection of key-value pairs, where each key is unique.
