# ## 🔢 Level 1 — Basics & Arithmetic

# 1. Take two numbers as input and print their **product, difference, and quotient**.
# 2. Input the **radius of a circle** and print its area and circumference. _(Use `math.pi`)_
# 3. Input a **temperature in Celsius** and convert it to Fahrenheit.
# 4. Input a person's **weight (kg) and height (m)** and calculate their BMI.
# 5. Input the **length and breadth** of a rectangle and print its area and perimeter.

# 1. 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(num1 * num2)
print(num1 - num2)
print(num1 / num2)


#2.
from math import pi

rad = float(input("Enter the radius of the circle: "))
area = (pi * rad * rad)
circumference = ( 2* pi * rad )

print(f"The circle which has the {rad} is having the area of {area} and the circumference of {circumference}.")

#3. 
temp = float(input("Enter your temperature in Celsius: "))
Fah = (temp * 9/5) + 32
print(f"The temperature of {temp} in Celsius is {Fah} in Fahrenheit.")

#4. 
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight / (height * height)
print(f"Your BMI is {BMI}")

#5.
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth) 
print(f"The area of rectangle is {area} and the perimeter is {perimeter}")