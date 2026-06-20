#  functions

# earlier we were writing code like this :
a = 10
b = 23
sum = a+b
print(sum)


# but now we will use
def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,6)

# function definition
def calculate_sum(a,b): #parameters
    return a+b
print(calculate_sum(5,6)) #function call ; arguments


# wap to calculate avg of three numbers:
def cal_avg(a,b,c):
    return (a+b+c)/3
print(cal_avg(int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(input("Enter the third number: "))))


# dafault parameters
def cal_prod (a,b=9):
    return a*b
print(cal_prod(5))