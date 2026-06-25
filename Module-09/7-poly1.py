# Polymorphism
#  Operator overriding
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        print(f"{self.real}i + {self.imag}j")

    def __add__(self, num2):
        new_real = self.real + num2.real
        new_imag = self.imag + num2.imag
        return Complex(new_real, new_imag)

a = Complex(2, 3)
a.show_number()
num2 = Complex(3, 4)
num2.show_number()

c = a.__add__(num2)
c.show_number()
d =a+num2
d.show_number()