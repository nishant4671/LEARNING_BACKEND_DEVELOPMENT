# what is a init method in python 
# In Python, the `__init__` method is a special method that is called when an instance (object) of a class is created. It is commonly referred to as the constructor of the class. The purpose of the `__init__` method is to initialize the attributes of the newly created object.




# basic example of using the `__init__` method:



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# The __init__ method initializes the name and age attributes of the Person class.
# With __init__:

# Every object starts in a valid, predictable state

# Enforces required data



# Key Points to Remember

# Name must be exactly __init__

# First parameter is always self

# Does not return anything

# Runs once per object creation



# Common mistakes

# ❌ Returning a value:

def __init__(self):
    return 5   # ❌ error


# ❌ Forgetting self:

def __init__(name):
    pass




# Analogy (easy to remember)

# Class → Blueprint of a house

# __init__ → Interior setup (rooms, wiring, furniture)

# Object → Actual house you live in



# The __init__ method is a constructor that initializes an object’s attributes when the object is created.