# As your programs grow, putting all your code in one file becomes messy and unmaintainable. Imagine writing a book in a single, gigantic paragraph. Modules and packages are how we structure our code into logical, reusable units.






# A module is simply a file containing Python code. It can define functions, classes, and variables. You can create your own modules or use built-in ones.
# A package is a collection of related modules organized in directories. It allows for a hierarchical structuring of the module namespace using dot notation.
# To use a module or package, you import it using the import statement.
# For example, to use the math module, you would write:
import math

result = math.sqrt(16)


# Module: A single Python file (.py) containing definitions (functions, classes, variables) that you can use in another Python file. It's a toolbox.

# Example: math_operations.py could contain add(), subtract(), multiply() functions.

# Package: A collection of modules organized in a directory. A package must contain a special file named __init__.py (which can be empty). It's a toolbox drawer.



# Import the entire module
import math
print(math.sqrt(25))  # 5.0

# Import a specific function/class
from datetime import datetime
print(datetime.now())

# Import with an alias (common for long names)
import numpy as np 
 



# The Standard Library: Python comes with a vast collection of built-in modules for common tasks (os, sys, datetime, random, json). You don't need to install them.

# Virtual Environment (venv): A self-contained directory that contains a Python installation for a particular project, plus its dependencies. This prevents conflicts between project requirements. It's a project-specific sandbox.


# to craete a vitual enviroment # python -m venv myenv

# To activate the virtual environment:
# On Windows: myenv\Scripts\activate

