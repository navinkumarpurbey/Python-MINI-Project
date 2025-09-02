# Python Countdown Timer with Start/Stop ⏳

# Python Countdown Timer with Start/Stop ⏳

import time
import threading

running = False  # flag to control the timer

def countdown_timer(seconds):
    global running
    running = True
    print(f"⏰ Countdown started for {seconds} seconds...\n")

    while seconds and running:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    if running:
        print("\n🎉 Time's up!")
    else:
        print("\n⏹ Countdown stopped by user.")

def main():
    global running
    while True:
        print("\nOptions:")
        print("1. Start Timer ▶️")
        print("2. Stop Timer ⏹")
        print("3. Exit 🚪")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            seconds = int(input("Enter time in seconds: "))
            timer_thread = threading.Thread(target=countdown_timer, args=(seconds,))
            timer_thread.start()

        elif choice == "2":
            running = False

        elif choice == "3":
            print("👋 Exiting...")
            break

        else:
            print("⚠ Invalid choice!")

# Run program
main()
