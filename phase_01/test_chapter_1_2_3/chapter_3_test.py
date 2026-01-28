# make a resuable module to use inventory restocking things in other files and all and multiple files 
def restock_item(inventory, item_name, additional_quantity):
    for item in inventory:
        if item["name"] == item_name:
            item["quantity"] += additional_quantity
            return f"Restocked {additional_quantity} units of {item_name}. New quantity: {item['quantity']}"
    return f"Item {item_name} not found in inventory."



# what this code does :
# This code defines a function restock_item that takes an inventory list, an item name, and an additional quantity to restock.
# It searches for the item in the inventory and updates its quantity if found, returning a confirmation message.
# If the item is not found, it returns a message indicating that the item is not in the inventory.
# Concepts used here :
# - Function Definition
# - Looping through a list
# - Conditional Statements (if)
# - Dictionary Access and Modification
# - Return Statements
# - String Formatting
# - List Manipulation
# - Searching in a list of dictionaries
#  how to import this module in other files :
# To use this module in other files, you can import it using the import statement. For
# example, if this code is saved in a file named inventory_utils.py, you can import and use the restock_item function as follows:
# from inventory_utils import restock_item
# inventory = [
#     {"name": "Steel Widget", "quantity": 120, "price_per_unit": 49.99, "supplier_ids": ["SUP001", "SUP014", "SUP021"]},

# example on how to use this in other file 
#     {"name": "Plastic Widget", "quantity": 80, "price_per_unit": 19.99, "supplier_ids": ["SUP002", "SUP015"]}
# ]
# result = restock_item(inventory, "Plastic Widget", 50)
# print(result)  # Output: Restocked 50 units of Plastic Widget. New quantity: 130
