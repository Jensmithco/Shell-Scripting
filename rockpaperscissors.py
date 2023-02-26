import random

bashanswer = input("rock, paper or scissors? ") 

possibleChoices = ["rock", "paper", "scissors"]
computerChoice = random.choice(possibleChoices)

if bashanswer == computerChoice:
    print("Both players selected {bashanswer}. It's a tie.")
elif bashanswer == "rock":
    if computerChoice == "scissors":
        print("Rock beats scissors. You win!")
    else:
        print("Paper beats rock. You lose.")
elif bashanswer == "paper":
    if computerChoice == "rock":
        print("Paper beats rock. You win!")
    else:
        print("Scissors beats paper. You lose.")
elif bashanswer == "scissors":
    if computerChoice == "paper":
        print("Scissors beats paper. You win!")
    else:
        print("Rock beats scissors. You lose.")
