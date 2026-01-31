# Define a class named InventoryItem.

# Its __init__ method must accept four parameters: name, quantity, price_per_unit, and supplier_ids.

# Inside __init__, assign each parameter to an instance attribute (e.g., self.name = name).

# Create an instance of InventoryItem using your sample data. Assign it to a variable named widget_obj.



class InventoryItem:
    def __init__(self, name, quantity, price_per_unit, supplier_ids): #here the self means the instance of the class
        self.name = name #this is how you assign the parameters to instance attributes
        self.quantity = quantity #
        self.price_per_unit = price_per_unit
        self.supplier_ids = supplier_ids

        # widget_obj = InventoryItem("Widget", 100, 2.50, [101, 102, 103])



        # example how this really works 
        theory = "If you create an instance of InventoryItem with the name 'Widget', quantity 100, price_per_unit 2.50, and supplier_ids [101, 102, 103], then the instance attributes will be set accordingly."

        # how to add other fucntions to this class 
    def total_value(self):
            return self.quantity * self.price_per_unit
        
        # exmaple of multiple fucntions in a class with init function as well 
    def add_stock(self, amount):
        self.quantity += amount
    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock to remove the requested amount.")


        
widget_obj = InventoryItem("Widget", 100, 2.50, [101, 102, 103])
item2 = InventoryItem("Gadget", 5, 10.0, ["SUP555"])
item2.add_stock(3)
print(item.quantity) # Output: 8
print(item2.total_value()) # Output: 80.0



        


        