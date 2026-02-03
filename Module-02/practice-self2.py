# write a program for traffic light system 
# where user has to enter the color and program has to tell the user what has to be done.

light = input("Enter the light: ")

if(light == "red" or light == "RED" or light == "Red"):
    print("STOP.!")
elif(light == "yellow" or light == "YELLOW" or light == "Yellow"):
    print("Look out")
elif(light == "green" or light == "GREEN" or light == "Green"):
    print("GO.!")
elif(light == "blue" or light == "Blue" or light == "BLUE" or light == "White" or light == "WHITE" or light == "White"):
    print("The light is broken.")
else:
    print("Wrong Color.")
print("Thank You.!")
print("="*12) 