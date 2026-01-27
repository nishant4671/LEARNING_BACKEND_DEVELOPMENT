import calculator 
import datetime
result = calculator.add(5, 3)
print("The sum is:", result)

result = calculator.multiply(5, 3)
print("The product is:", result)
print("Current date and time:", datetime.datetime.now())
print("the date for today is : ", datetime.date.today())


# here we have also imported a standard library datetime to show how to import from standard libraries

# in case calculator was in a different directory we would have to use sys.path.append to add that directory to the path like below
# example on how to import from different directory
# import sys
# sys.path.append('path_to_calculator_directory')
# import calculator
# here this was possible because calculatior function was in the same directory as main.py
# import os this library provides a way of using operating system dependent functionality, example to work with file paths
# print("Current Working Directory:", os.getcwd())


