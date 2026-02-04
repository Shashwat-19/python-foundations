#  write a program to check if the number which is entered by the user is odd or even.abs

num = int(input("Enter the number: "))

if (num % 2 == 0):
    print("The number is Even.")
elif(num % 2 != 0):
    print("The number is odd.")
else:
    print("Invalid Number.")

print("="* 29)