# # what is init.py file in python?
# # In Python, an `__init__.py` file is used to mark a directory as a Python package. When a directory contains this file, Python treats it as a package, allowing you to import modules from that directory.
# # The `__init__.py` file can be empty, but it can also execute initialization code for the package or set the `__all__` variable to define the public interface of the package. This file is essential for organizing code into reusable modules and packages, making it easier to manage larger codebases.
# # # An empty __init__.py file
# # # mypackage/__init__.py
# # # This file can be empty, or you can add initialization code here
# # # Example of using __init__.py to define a package
# # # mypackage/__init__.py
# # from .module1 import *
# # from .module2 import *
# # # Now you can import mypackage and access module1 and module2
# # Example of __init__.py with initialization code
# #!/usr/bin/env python3
# # mypackage/__init__.py
# print("Initializing the mypackage package")
# from .module1 import *
# from .module2 import *
# # Now you can import mypackage and access module1 and module2