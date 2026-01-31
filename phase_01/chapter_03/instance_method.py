# instance method example 
# his is the most common type.
# It uses self and can access/modify that specific object’s data.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):   # instance method
        print("Name:", self.name)
        print("Marks:", self.marks)


# use it 


s1 = Student("Aman", 90)
s2 = Student("Riya", 75)

s1.show_details()
s2.show_details()
