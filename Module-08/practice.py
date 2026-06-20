# wap to create a student class that takes name & marks of 3 subjects
# as an arguments in constructor.
# then create a method to print the average.
from torch.distributions import studentT


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum/len(self.marks)
s1 = Student("karan", [78,89,98])
print(s1.check_avg())
