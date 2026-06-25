# 1
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * (self.r ** self.r)

    def perimeter(self):
        return 2 * (self.r * self.r) * 3.14

c1 = Circle(float(input("Enter the radius of the circle: ")))
print(f"The area of the circle is {c1.area():.2f}")
print(f"The perimeter of the circle is {c1.perimeter():.2f}")


# 2
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_Details(self):
        print(f"The role is {self.role} from the department of {self.department} with a salary of Rs {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 98790)


e1 = Employee("Accountant", "Accounts", 56730)
e1.show_Details()
en2 = Engineer("Shashwat", "22")
en2.show_Details()


# 3
class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("Tea", 100)
odr2 = Order("shoes", 200)
print(odr1.price)
print(odr2.price)
print(odr1>odr2)