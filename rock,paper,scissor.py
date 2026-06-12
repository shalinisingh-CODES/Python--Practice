import random

item_list = ["rock", "paper", "scissor"]
user_choice = input("Enter your move = rock, paper, scissor: ")
comp_choice = random.choice(item_list)

print(f"User choice= {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chose the same: match tie")
elif user_choice == "rock":
    if comp_choice == "paper":
        print("Computer wins")
    else:
        print("You win")
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Computer wins")
    else:
        print("You win")
elif user_choice == "scissor":
    if comp_choice == "rock":
        print("Computer wins")
    else:
        print("You win")
else:
    print("Invalid input! Please type rock, paper, or scissor")

    
