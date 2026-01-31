# 3️⃣ Static Method (just a helper function inside class)

# Uses @staticmethod.

# It does not use self or cls.
# It doesn’t care about object data or class data.



class Student:
    @staticmethod
    def is_pass(marks):   # static method
        return marks >= 40
# use it

print(Student.is_pass(50))   # True
print(Student.is_pass(30))   # False
# Static methods are used as utility functions that have some logical connection with the class.
print(Student.is_pass(75))   # True
print(Student.is_pass(20))   # False
# They don’t need to access or modify class or instance data.
