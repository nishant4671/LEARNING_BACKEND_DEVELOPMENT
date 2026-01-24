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




# Python **dictionaries (`dict`)** are one of the most important data structures, especially for **backend development** (Django/DRF). They store data in **Key → Value** form.

# ---

# ## ✅ 1) What is a Dictionary?

# A dictionary is a collection of **key-value pairs**.

# ### Example:

# ```python
# student = {
#     "name": "Nishant",
#     "age": 19,
#     "branch": "IT"
# }
# ```

# ✅ Keys are used to **access values instantly (fast lookup)**.

# ---

# ## ✅ 2) Why Dictionaries are used so much?

# Because they represent **real-world structured data**, like:

# ✅ User profile
# ✅ API JSON data
# ✅ Database-like records
# ✅ Settings/config values
# ✅ Frequency counting (most common use in coding)

# Example JSON from API looks like dict:

# ```python
# data = {
#     "id": 12,
#     "username": "nishant4671",
#     "is_active": True
# }
# ```

# ---

# ## ✅ 3) Creating a Dictionary

# ### Method 1: Normal

# ```python
# person = {"name": "Aman", "age": 21}
# ```

# ### Method 2: Using dict()

# ```python
# person = dict(name="Aman", age=21)
# ```

# ---

# ## ✅ 4) Accessing Values

# ### Direct access

# ```python
# print(person["name"])
# ```

# ⚠️ If key doesn't exist → **KeyError**

# ### Safe access using `.get()`

# ```python
# print(person.get("city"))
# ```

# With default value:

# ```python
# print(person.get("city", "Not Found"))
# ```

# ✅ `.get()` is used a LOT in backend to avoid crashing.

# ---

# ## ✅ 5) Adding / Updating Values

# ```python
# person["city"] = "Delhi"   # add new key
# person["age"] = 22         # update existing key
# ```

# ---

# ## ✅ 6) Removing Keys

# ### Using `del`

# ```python
# del person["age"]
# ```

# ### Using `.pop()`

# ```python
# person.pop("city")
# ```

# ✅ `.pop()` returns removed value too.

# ---

# ## ✅ 7) Checking if Key exists (VERY IMPORTANT)

# ```python
# if "name" in person:
#     print("Name exists")
# ```

# ---

# ## ✅ 8) Looping Through Dictionary

# ### Loop keys only

# ```python
# for key in person:
#     print(key)
# ```

# ### Loop values only

# ```python
# for value in person.values():
#     print(value)
# ```

# ### Loop key + value

# ```python
# for key, value in person.items():
#     print(key, "=>", value)
# ```

# ✅ `.items()` is the most useful.

# ---

# ## ✅ 9) Dictionary Methods You Must Know

# ### `.keys()`

# ```python
# print(person.keys())
# ```

# ### `.values()`

# ```python
# print(person.values())
# ```

# ### `.items()`

# ```python
# print(person.items())
# ```

# ### `.update()`

# ```python
# person.update({"age": 25, "country": "India"})
# ```

# ---

# ## ✅ 10) Nested Dictionaries (Backend Level)

# Very common in APIs.

# ```python
# user = {
#     "id": 1,
#     "profile": {
#         "name": "Nishant",
#         "skills": ["Python", "Django"]
#     }
# }
# ```

# Access:

# ```python
# print(user["profile"]["skills"][0])  # Python
# ```

# ---

# ## ✅ 11) Most Important Use Case: Frequency Count

# Example: Count letters in a string

# ```python
# s = "banana"
# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1

# print(freq)
# # {'b': 1, 'a': 3, 'n': 2}
# ```

# ✅ This pattern is GOLD in DSA + backend.

# ---

# ## ✅ 12) Dictionary Comprehension (Advanced but useful)

# ```python
# nums = [1, 2, 3, 4]
# squares = {x: x*x for x in nums}
# print(squares)
# # {1:1, 2:4, 3:9, 4:16}
# ```

# ---

# ## ✅ 13) Common Backend Uses (Real Django/DRF)

# ### Example: Django serializer output (looks like dict)

# ```python
# response_data = {
#     "status": "success",
#     "data": {"id": 1, "username": "nishant"}
# }
# ```

# ✅ Then API returns JSON from it.

# ---

# # ✅ Quick Summary

# ✅ Dict = Key-Value store
# ✅ Fast lookup
# ✅ Used for JSON, API data, configs
# ✅ Used for frequency counting and caching

# ---

