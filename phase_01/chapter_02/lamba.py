# Topic 2.1 (Continued): Functions - Lambda & Map/Filter
# A. Micro-Lesson: Anonymous Functions and Functional Tools
# Sometimes, you need a simple, one-line function for a short-lived purpose. Writing a full def statement feels cumbersome. This is where lambda functions come in.

# Lambda Function: A small, anonymous (unnamed) function defined with the lambda keyword. It can take any number of arguments but can only have one expression, which is automatically returned.


# Traditional function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(square(5))        # 25
print(square_lambda(5)) # 25

