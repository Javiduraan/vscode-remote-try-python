#Create a rock paper scissors game with Python
# 1. Have the computer pick a random number between 1-3
# 2. Have the user pick a number between 1-3
# 3. Compare the two numbers
# 4. Print out a message to the user saying who won
# 5. Allow the user to play again if they want to
# 6. Keep track of how many wins the user has
# 7. Keep track of how many wins the computer has

import random

computer_wins = 0
user_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please enter a valid input")
        continue
    
    random_number = random.randint(0, 2)
    #0 is rock
    #1 is paper
    #2 is scissors
    if random_number == 0:
        computer_pick = "rock"
    elif random_number == 1:
        computer_pick = "paper"
    else:
        computer_pick = "scissors"
    
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")


