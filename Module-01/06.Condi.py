#  Conditional Statement

# Traffic Light
light = input("color: ")

if(light == "red" or "Red" or "RED"):
    print("STOP.!")
elif(light == "yellow" or "Yellow" or "YELLOW"):
    print("Look Carefully.")
elif(light == "green" or "Green" or "GREEN"):
    print("GO.")
else:
    print("The light is broken.")   


# Grades
marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("You got A grade")
elif(marks >=80 and marks <= 90):
    print("You got B grade.")
elif(marks >= 70 and marks <= 79):
    print("You got C grade.")
elif(marks >= 60 and marks <= 69):
    print("You got D grade.")
else:
    print("You got F grade.")