# Topic 2.1: Functions
# A. Micro-Lesson: The Anatomy of a Python Function
# A function is not just for reuse; it is a tool for abstraction. It allows you to define a single, clear action or calculation, give it a name, and hide its internal complexity. Think of it like a coffee machine. You don't need to know about water pumps, heating elements, or grinders. You provide inputs (beans, water) and press a button (espresso()). The machine executes a complex series of steps and returns the output. Your main program just calls espresso().

# Core Components:

# Definition: def keyword, function name, parentheses () for parameters, a colon :.

# Parameters: Variables listed inside the parentheses. These are the function's "promises" for what input it needs. They are local to the function.

# Body: The indented block of code that runs when the function is called.

# Return Value: The return statement sends a result back to the line that called the function. A function without a return implicitly returns None.





# Function Definition
def calculate_net_price(gross_price, tax_rate):
    """Calculate the net price after tax."""  # Docstring: explains the function's purpose
    tax_amount = gross_price * (tax_rate / 100)
    net_price = gross_price - tax_amount
    return net_price  # The OUTPUT is sent back

# Function Calls (Using the machine)
invoice_total = calculate_net_price(100, 20)  # 100 USD, 20% tax
print(f"Net Price: ${invoice_total}")  # Output: Net Price: $80.0

# We can call it again with different inputs (Reusability)
another_item = calculate_net_price(50, 10)
print(f"Another Item: ${another_item}")  # Output: Another Item: $45.0





#  Functions in Python are very flexible, but there are **some strict rules + important constraints** you must follow (especially for clean backend/industrial code).

# ---

# ## ✅ 1) Function name rules

# ### Must follow valid identifier rules:

# ✅ Can contain: letters, numbers, `_`
# ✅ Cannot start with a number
# ✅ Cannot use spaces
# ✅ Cannot be a keyword

# ✅ Correct:

# ```python
# def calculate_total():
#     pass

# def get_user2():
#     pass
# ```

# ❌ Wrong:

# ```python
# def 2total():      # starts with number
#     pass

# def class():       # keyword
#     pass
# ```

# ---

# ## ✅ 2) Indentation is mandatory

# Python uses indentation to define function body.

# ✅ Correct:

# ```python
# def greet():
#     print("Hello")
# ```

# ❌ Wrong:

# ```python
# def greet():
# print("Hello")  # IndentationError
# ```

# ---

# ## ✅ 3) Order of arguments (VERY IMPORTANT RULE)

# Python has a strict order in function parameters:

# ✅ Correct order:

# 1. **Normal parameters**
# 2. `*args`
# 3. **Keyword-only parameters**
# 4. `**kwargs`

# Example:

# ```python
# def func(a, b, *args, c=10, **kwargs):
#     pass
# ```

# ❌ Wrong:

# ```python
# def func(*args, a):   # invalid
#     pass
# ```

# ---

# ## ✅ 4) Default arguments rule

# If you give a default value to a parameter, **all parameters after it must also have defaults**.

# ✅ Correct:

# ```python
# def login(user, role="student"):
#     pass
# ```

# ❌ Wrong:

# ```python
# def login(user="guest", role):
#     pass
# ```

# ---

# ## ✅ 5) Mutable default values are dangerous (BIGGEST TRAP)

# ❌ Wrong:

# ```python
# def add_item(item, items=[]):
#     items.append(item)
#     return items
# ```

# This causes the list to be reused across calls.

# ✅ Correct:

# ```python
# def add_item(item, items=None):
#     if items is None:
#         items = []
#     items.append(item)
#     return items
# ```

# ---

# ## ✅ 6) Return rule

# A function can return:

# * one value
# * multiple values (as tuple)
# * or nothing

# If you don’t write `return`, Python returns `None`.

# Example:

# ```python
# def test():
#     print("Hi")

# print(test())  # None
# ```

# ---

# ## ✅ 7) Variable scope rules

# ### Local variables stay inside the function

# ```python
# def f():
#     x = 10

# # print(x)  # NameError
# ```

# ### Global variables can be read inside function

# ```python
# x = 5
# def f():
#     print(x)
# ```

# ### To modify global variable, you need `global`

# ```python
# x = 5
# def change():
#     global x
#     x = 100
# ```

# ⚠️ In industry: avoid `global` unless absolutely necessary.

# ---

# ## ✅ 8) Keyword arguments rules

# Keyword arguments must come **after positional arguments** when calling a function.

# ✅ Correct:

# ```python
# def add(a, b):
#     return a + b

# add(5, b=10)
# ```

# ❌ Wrong:

# ```python
# add(a=5, 10)  # SyntaxError
# ```

# ---

# ## ✅ 9) You can’t have duplicate parameter names

# ❌ Wrong:

# ```python
# def f(a, a):
#     pass
# ```

# ---

# ## ✅ 10) Recursion constraint (stack limit)

# Python has a recursion limit (default around ~1000).

# Example:

# ```python
# import sys
# print(sys.getrecursionlimit())
# ```

# If recursion gets too deep → `RecursionError`.

# ---

# ## ✅ 11) Function should not depend on hidden state (best practice)

# Bad:

# ```python
# x = 10
# def f():
#     return x + 1
# ```

# Better:

# ```python
# def f(x):
#     return x + 1
# ```

# ✅ Makes testing and debugging easier.

# ---

# ## ✅ 12) Type hints are optional but recommended

# ```python
# def add(a: int, b: int) -> int:
#     return a + b
# ```

# Helps:
# ✅ readability
# ✅ editor autocomplete
# ✅ reduces mistakes

# ---

# # ✅ Quick Summary (Most Important Rules)

# ✅ Correct naming + indentation
# ✅ Default args must come last
# ✅ Avoid mutable defaults (`[]`, `{}`)
# ✅ Positional before keyword in function calls
# ✅ Variables inside functions are local
# ✅ No return → returns `None`
# ✅ Recursion has limits






