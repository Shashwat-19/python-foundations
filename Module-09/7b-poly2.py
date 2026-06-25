# Polymorphism
# Function Overriding

class Employee:
    def get_desig(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_desig(self):
        print("Designation = Teacher")

t1 = Teacher()
t1.get_desig()


# Duck TYping
class Accountant:
    def get_desig(self):
        print("Designation = Accountant")

a1 = Accountant()
a1.get_desig()