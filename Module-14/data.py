import csv
students_data = []
with open("data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students_data.append(row)

for student in sorted(students_data, key=lambda student: student["name"]):
    print(f"Student Name: {student['name']}, Age: {student['age']}")