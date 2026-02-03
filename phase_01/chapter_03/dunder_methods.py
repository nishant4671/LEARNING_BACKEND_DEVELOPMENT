# These are also called magic methods or special methods.

# They are not meant to be called directly by you most of the time.
# Python calls them automatically to give your objects special behavior.


class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __str__(self):
        return f"Point at ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(p)           # Uses __str__: "Point at (3, 4)"
print(str(p))      # Same: "Point at (3, 4)"
print(repr(p))     # Uses __repr__: "Point(x=3, y=4)"

# In REPL:
# >>> p
# Point(x=3, y=4)  # Shows __repr__