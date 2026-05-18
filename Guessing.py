import random 

unknown_number = random.randint(1,50)
attempts = 0

print("NUMBER GUESSING GAME!!")
print("choose between 1 to 50")
print("READY")
print("    SET")
print("      GUESSSSSSS!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1 

    if guess > unknown_number:
        print("Slow Down!")
    elif guess < unknown_number:
        print("Goooo Higher!")
    else:
        print("YOU GOT IT!")
        break 