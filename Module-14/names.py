name = input("What's your name: ")
print(f"Hello, {name}!")

name = []

for i in range(3):
    name.append(input("What's your name: "))

for name in sorted(name):
    print(f"Hello, {name}!")


# now i want to save the data
name = input("Enter a name: ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

# using with statement to open the file
name = input("Enter a name: ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# readlines() method to read the file
with open("names.txt", "r") as file:
    # names = file.readlines()
    for name in sorted(file.readlines()):
        print(f"Hello, {name.rstrip()}!")
        #rstrip() method is used
        # to remove the newline character from the end of each name



names = []
with open("names.txt", "r") as file:
    for name in file.readlines():
        names.append(name.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}!")