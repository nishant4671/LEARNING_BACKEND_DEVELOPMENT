
# Challenge 2: The Function & Control Flow (from Chapter 2)
# Write a function called check_restock.

# It should take your item data structure (from Challenge 1) as an input.

# If the quantity is less than 10, it should return a formatted string: "[Item Name] is low in stock. Only [quantity] left."

# Otherwise, it should return the string: "[Item Name] is sufficiently stocked."



















def check_restock(widget):
    restock_threshold = 10
    if widget["quantity"]< restock_threshold:
        return f"{widget['name']} is low in stock only {widget[quantity]} is left ."
    else:
        return f"{widget['name']} is sufficiently stocked"
    




# return f"{widget['name']} is low in stock only {widget[quantity]} is left   this is how we fomat a string 

# concepts used here 
# # - Function Definition
# # - Conditional Statements (if-else)
# # - String Formatting
# dictionaries 
# # - Accessing Dictionary Values
# - Comparison Operators
