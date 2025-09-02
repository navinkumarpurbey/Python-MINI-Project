import random

# Choices
choices = ["rock", "paper", "scissors"]

# User input
user_choice = input("Enter rock, paper or scissors: ").lower()

# Computer choice
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Game logic
if user_choice == computer_choice:
    print("It's a Tie! 😮")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("🎉 You Win!")
else:
    print("💻 Computer Wins!")
