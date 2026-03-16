# ## 🔀 Level 2 — Conditionals

# 6. Input a **year** and check if it's a **leap year**.
# 7. Input **three sides of a triangle** and check if it's valid _(sum of any two sides > third)_.
# 8. Input a **character** and check if it's a **vowel or consonant**.
# 9. A shopkeeper gives discount based on purchase amount:
#    - Above ₹5000 → 20% off
#    - ₹2000–₹5000 → 10% off
#    - Below ₹2000 → No discount

#    Print the **final amount payable**.

# 10. Input a number and check if it's **positive, negative, or zero**.

#6.
year = int(input("Enter the year: "))
if (year % 4 == 0):
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not a leap year.")


#7. 
side_a = float(input("Enter the first side of the Triangle: "))
side_b = float(input("Enter the second side of the Triangle: "))
side_c = float(input("Enter the third side of the Triangle: "))

if (side_a + side_b > side_c or side_b + side_c > side_a or side_a + side_c > side_c):
    print("This triangle is valid.")
else:
    print("The triangle is not valid.")

#8. 
char = input("Enter the character: ")
if (char == "a","e","i","o","u"):
    print(f"The character {char} is a Vowel.")
else:
    print(f"The character {char} is a Consonant.")

#9. 
amount = float(input("Enter the Amount in RS: "))
if(amount > 5000):
    print("You will get 20% off where your final amount will be: " , amount - (20/100 - amount))
elif( 2000 < amount < 5000):
    print("You will get 10% off where your final amount will be: " , amount - (10/100 - amount))
else:
    print(f"Your final amount is {amount}")

#10.
num = int(input("Enter the number: "))
if(num > 0):
    print(f"The number {num} is Positive.")
elif(num<0):
    print(f"The number {num} is Negative.")
else:
    print(f"The number {num} is Zero.")
q