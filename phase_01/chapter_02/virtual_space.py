# # 1. CREATE the isolated box (in your project folder)
# python -m venv venv

# # # 2. ENTER the box
# # # On Windows:
# # venv\Scripts\activate
# # # On Mac/Linux:
# # source venv/bin/activate
# # # (Your terminal prompt will change, showing '(venv)')

# # # 3. INSTALL packages inside the box
# # pip install django==4.2.0 requests

# # # 4. FREEZE your package list for replication
# # pip freeze > requirements.txt  ">" means redirect output to a file , in this case requirements.txt will get the package list 
# what does this  freeze do ?
# The `pip freeze` command generates a list of all the installed packages in your current Python environment along with their versions. When you redirect this output to a file using `> requirements.txt`, it creates a file named `requirements.txt` that contains this list.
# This file can then be used to replicate the same environment on another machine by installing the exact versions of the packages listed in it.



# # # 5. TO REPLICATE the environment on another machine:
# # # Create the isolated box
# # python -m venv venv
# # # Enter the box
# # # On Windows:
# # venv\Scripts\activate




# To share your project: Include requirements.txt. Others run pip install -r requirements.txt inside their own virtual environment.






