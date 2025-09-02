import random

print("🎲 Welcome to Dice Roller Simulator 🎲")

while True:
    # Roll the dice
    dice = random.randint(1, 6)
    print(f" You rolled: {dice} 🎲")
    
    # Ask user to roll again or exit
    choice = input("Roll again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing! Goodbye 👋")
        break
