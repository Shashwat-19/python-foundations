# Try and Except block to handle exception
# ==========================
try:
    x = int(input("What is x: "))
except ValueError:
    print("Please enter a number.")
else:
    print(f"x is: {x}")
# ==========================

# Better way to handle exception is to use while loop with try and except block
# ==========================
while True:
    try:
        x = int(input("What is x: "))
    except ValueError:
        print("Please enter an integer number.")
    else:
        break
print(f"x is: {x}")
# ==========================

# More better way to handle exception is to use function with while loop with try and except block
# ==========================
def main():
    x = get_int()
    print(f"x is: {x}")

def get_int():
    while True:
        try:
            return int(input("What is x: "))
        except ValueError:
            print("Please enter an integer number.")
        else:
            return x

main()
# ==========================

# using function with while loop with try and except block with pass
# ==========================
def main():
    x = get_int()
    print(f"x is: {x}")

def get_int():
    while True:
        try:
            return int(input("What is x: "))
        except ValueError:
            pass

main()
# ==========================

# using function with while loop with try and except block with pass and prompt message
# ==========================
def main():
    x = get_int("What's x?: ")
    print(f"x is: {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
# ==========================

