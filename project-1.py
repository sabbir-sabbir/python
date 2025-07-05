# 1 for snake
# -1 for water
# 0 for gun
import random

computer = random.choice([-1, 0, 1])
user = input("Enter your choise; ")

user_Input_Dict = {"s": 1, "w": -1, "g": 0}
reverse_Dict = {1: "snake", -1: "water", 0: "gun"}

yourNumber = user_Input_Dict[user]
print(f"You chose {reverse_Dict[yourNumber]} _ Computer chose {reverse_Dict[computer]}")

if(computer == yourNumber):
    print("Its Draw")
elif(computer == -1 and yourNumber == 1):
    print("User is win!")
elif(computer == -1 and yourNumber == 0):
    print("User lose!")    
elif(computer == 1 and yourNumber == -1):
    print("You lose!")    
elif(computer == 1 and yourNumber == 0):
    print("User win!")    
elif(computer == 0 and yourNumber == -1):
    print("Computer win!")   
else:
    print("something went worng!")     

