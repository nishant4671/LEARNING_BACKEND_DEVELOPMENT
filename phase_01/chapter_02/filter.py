# ✅ filter() = “KEEP only some items”

# It takes a list and removes items you don’t want, based on a condition.



numbers = [1, 2, 3, 4, 5]

greater_than_2 = list(filter(lambda x: x > 2, numbers))
print(greater_than_2)   # [3, 4, 5]


