import random

def StartGame():
    RandomInt = random.randint(1, 100)
    UserInt = -1
    Guess = 0

    while (UserInt != RandomInt):
        Guess += 1
        UserInt = int(input("Enter a number to find the random number(*_*):  "))
        if (UserInt > RandomInt):
            print("Enter Lower Number Please !!")
        else:
            print("Enter Higher number Please !!")

    if (Guess > 10):
        print(f"You done this game at {Guess} guesses. You need more practice ############ Be Focus !!!!!!! ")
    else:
        print(f"You done this game less than 10 guesses. Very Impressive (*_*) (*_*) (*_*) (*_*)")

while True:
    StartGame()
    choice = input("Press Enter to exit or press 'A' to play again: ").strip().lower()
    if choice == 'a':
        continue
    else:
        break






