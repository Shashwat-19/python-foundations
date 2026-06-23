# Inheritance

# Single-Level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

# car1 = Toyota(input("Enter car name: "))
# print(car1.name)
# car1.start()
# car1.stop()


# Multi-Level Inheritance
class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

c2 = Fortuner("diesel")
print(c2.type)
c2.start()



# Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

C1 = C()
print(C1.varA)