class Restaurant:
    # CLASS ATTRIBUTE - Shared by all restaurants of this chain
    menu_type = "Standard"  # This belongs to the blueprint, not a single restaurant
    
    def __init__(self, name, tables):
        # INSTANCE ATTRIBUTES - Unique to each restaurant
        self.name = name
        self.tables = tables
    
    # INSTANCE METHOD - Acts on a specific restaurant
    def serve_table(self, table_number):
        return f"Serving table {table_number} at {self.name}"
    
    # CLASS METHOD - Acts on the class itself (the blueprint)
    @classmethod
    def change_menu_type(cls, new_type):
        cls.menu_type = new_type  # 'cls' is Restaurant (the class)
        return f"All restaurants now have {new_type} menu"
    
    # STATIC METHOD - Just a utility, needs no access to instance or class
    @staticmethod
    def calculate_tax(amount):
        return amount * 0.08  # Just a calculation, doesn't need 'self' or 'cls'

# Using them:
# Instance method needs an instance
my_restaurant = Restaurant("Tasty Bites", 10)
print(my_restaurant.serve_table(3))  # "Serving table 3 at Tasty Bites"

# Class method works on the class
print(Restaurant.change_menu_type("Vegetarian"))  # Changes for ALL restaurants
print(Restaurant.menu_type)  # "Vegetarian"
print(my_restaurant.menu_type)  # Also "Vegetarian" - it's shared!

# Static method can be called on class OR instance
print(Restaurant.calculate_tax(100))  # 8.0
print(my_restaurant.calculate_tax(100))  # Also 8.0
restaurant2 = Restaurant("Quick Eats", 5)
print(restaurant2.menu_type)  # "Vegetarian" - reflects class change

# Demonstrates instance, class, and static methods in a restaurant context



