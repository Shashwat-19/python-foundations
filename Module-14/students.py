with open("students.csv", "a") as file:
    name = input("Enter a student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    file.write(f"{name},{age},{grade}\n")

with open("students.csv", "r") as file:
    for line in sorted(file.readlines()):
        name, age, grade = line.rstrip().split(",")
        print(f"Student Name: {name}, Age: {age}, Grade: {grade}")