# Simple Python Text Adventure Game 🎮

def start_game():
    print("Welcome to the Adventure Game! 🚀")
    print("You are standing at a crossroad. Where do you want to go?")
    print("1. Left towards the forest 🌲")
    print("2. Right towards the river 🌊")

    choice1 = input("Enter 1 or 2: ")

    if choice1 == "1":
        print("\nYou enter a dark forest... 🌲")
        print("You see a glowing light ahead. Do you:")
        print("1. Follow the light 🔦")
        print("2. Stay on the path 🛤️")

        choice2 = input("Enter 1 or 2: ")

        if choice2 == "1":
            print("\nYou found a hidden treasure! 🏆 You Win! 🎉")
        else:
            print("\nA wild wolf appears! 🐺 You lose. 💀")

    elif choice1 == "2":
        print("\nYou reach the river... 🌊")
        print("Do you want to:")
        print("1. Swim across 🏊")
        print("2. Build a raft 🛶")

        choice2 = input("Enter 1 or 2: ")

        if choice2 == "1":
            print("\nThe current is too strong! 🌊 You drown. 💀")
        else:
            print("\nSmart choice! 🚀 You cross safely and find treasure! 🏆 You Win! 🎉")
    else:
        print("\nInvalid choice. Game Over! ❌")


# Run the game
start_game()
