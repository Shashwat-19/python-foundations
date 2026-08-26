import csv
name = input("Enter a student's name: ")
home = input("Enter the student's home: ")
with open("home.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
