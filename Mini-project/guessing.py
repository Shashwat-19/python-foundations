import random

num = random.randint(1, 100)
while True:
    guess = input("Guess a number: ")
    if guess != "exit":
        guess = int(guess)
        if guess == num:
            print("You guessed the number")
            break
        elif guess > num:
            print("Too high")
            continue
        elif guess < num:
            print("Too low")
            continue
    else:
        print("Exiting")
        break
print("Thank you for playing")