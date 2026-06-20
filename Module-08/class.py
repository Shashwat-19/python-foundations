# class

class Student:

    # default constructor
    # def __init__(self):
    #     pass
    college_name = "ABC College" # class attribute
    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #decorator
    def welcome1(cls):
        print(cls.college_name)

    @staticmethod #decorator
    def college():
        print(f"I am from {Student.college_name}")

    def welcome(self): #methods
        print(f"Welcome to this class {self.name}")

    def age(self):
        return self.age

s1 = Student("karan", 20)
print(s1.name, s1.age, s1.college_name)
s1.welcome()
s1.college()
s1.welcome1()





# class Car_factory:
#     color = "Black"
#     brand = "BMW"
#
# c1 = Car_factory()
# print(c1.color)
# print(c1.brand)