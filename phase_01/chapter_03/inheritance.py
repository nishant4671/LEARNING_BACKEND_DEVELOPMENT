# Add a "private" attribute __discount (using double underscores) in the __init__ method, with a default value of 0.1 (10%).

# In Python, a private attribute is created by prefixing it with a single underscore to indicate internal use, or with a double underscore to trigger name mangling and reduce accidental access. Python relies on conventions rather than strict access control.


class InventoryItem:
    def __init__(self, name, quantity, price_per_unit, supplier_ids): #here the self means the instance of the class
        __discount = 0.1 #is this how you create a private attribute
        # properties of a private attribute



        self.name = name #this is how you assign the parameters to instance attributes
        self.quantity = quantity #
        self.price_per_unit = price_per_unit
        self.supplier_ids = supplier_ids
        self.__discount = __discount        

    # Add a method get_discounted_price(self) that returns the price_per_unit after applying the discount (i.e., price_per_unit * (1 - self.__discount)).
    # 
    def get_discounted_price(self):
        return self.price_per_unit * (1 - self.__discount)
    #     example how this really works
    # theory = "If you create an instance of InventoryItem with the name 'Widget', quantity 100, price_per_unit 2.50, and supplier_ids [101, 102, 103], then the instance attributes will be set accordingly."




# Part 2 - Inheritance:
# Create a new class PerishableItem that inherits from InventoryItem.

# Its __init__ method should accept all the parameters of InventoryItem plus an additional expiry_date (a string like "2024-12-31").

# Use super().__init__(...) to initialize the inherited attributes correctly.

# Override the total_value method. If the expiry_date is before "2024-05-01" (hardcoded for this exercise), return 0. Otherwise, calculate the total value normally (quantity * price_per_unit).

class perishableItem(InventoryItem):
    def __init__(self, name, quantity, price_per_unit, supplier_ids, expiry_date):
        super().__init__(name, quantity, price_per_unit, supplier_ids)
        self.expiry_date = expiry_date

    def total_value(self):
        if self.expiry_date < "2024-05-01":
            return 0
        else:
            return self.quantity * self.price_per_unit
        



# example usage of this 
perishable_item = perishableItem("Milk", 50, 1.5, [201, 202], "2024-04-30")

# theory for thr inhertitance syntax here 
# theory = "The PerishableItem class inherits from InventoryItem. It adds an expiry_date attribute and overrides the total_value method to account for items that have expired."
# # print(perishable_item.total_value())  # Output: 0 since the expiry_date is before "2024-05-01"
print(perishable_item.total_value())  # Output: 0 since the expiry_date is before "2024-05-01"
print(perishable_item.get_discounted_price())  # Output: 1.35 (1.5 * (1 - 0.1))
