# 2️⃣ Class Method (works on the whole class)

# Uses @classmethod and takes cls instead of self.

# It is used when something belongs to the class itself, not individual objects.

class Student:
    school_name = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):   # class method
        cls.school_name = new_name
# use it



s1 = Student("Aman")
s2 = Student("Riya")

print(Student.school_name)   # ABC School

Student.change_school("XYZ School")

print(Student.school_name)   # XYZ School
print(s1.school_name)        # XYZ School
print(s2.school_name)        # XYZ School




# One change affects all students, because it changed the class data.