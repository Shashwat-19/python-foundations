# Propert Decorator

class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percentage(self):
        return str((self.math + self.phy + self.chem) / 3) + "%"

s1 = Student(98, 99, 97)
print(s1.percentage)

s1.phy = 78
print(s1.percentage)