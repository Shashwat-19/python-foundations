# 1
# Create a "Practice.txt" file and add "Hi everyone\nwe are learning File I/O\n using Java.\nI like programming in Java"
with open("practice.txt", "w+") as f:
    f.write("Hi everyone\nwe are learning File I/O\n using Java.\nI like programming in Java.")


#   Replace Java with Python
with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)

#  Show new data
with open("practice.txt", "w") as f:
     f.write(new_data)

# check if the word "learning" exists
word = "learning"
with open("practice.txt", "r") as f:
    while True:
        line = f.read()
        if "learning" in line:
            print("="*34)
            print(f"{word} exists.")
        break

# check at which line it exists
line_check = 1
word = "learning"
data = True
with open("practice.txt", "r") as f:
    while data:
        data = f.readline()
        if "learning" in data:
            print("="*34)
            print(f"{line_check} line number has the word {word}.")
            break
        line_check += 1


# from a file "sample.txt" numbers separated by comma, print the even numbers
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

    new_list = data.split(",")
    print(new_list)
    even = []
    count = 0
    for items in new_list:
        items = int(items)
        if items % 2 == 0:
            even.append(items)
            count += 1
    print(f"Even numbers are: {even}")
    print(f"Total even numbers are: {count}")

