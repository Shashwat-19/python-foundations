# 1
# WAP to print the length of the list. (list is the parameter)
list_here = [1,2,3,4,5,6,3,5]
def length(a):
    return len(a)
print(f"The length of the list = {list_here} is {length(list_here)}")


# 2
# WAP to print the elements of a list in a single line. (list is the parameter.)
list_again = [1,2,3,4,5,6,3,5,8]
def check_ele(list):
    for elements in list:
        print(elements, end = " ")
check_ele(list_again)


# 3
# WAP to find the factorial of n. (n is the parameter)
n = int(input("\nEnter any number: "))
def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact
print(f"The factorial of number {n} is {factorial(n)}")



# 4
# WAP to convert USB to INR
amount = int(input("Enter the amount: USD "))
def convert(a):
    return a * 94.33
print(f"The amount will be Rs {convert(amount):.2f}")


# homework
# wap to check if the number is odd or even
num = int(input("Enter a number: "))
def check_num(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(f"The number {num} is {check_num(num)}")