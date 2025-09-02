# Simple AI Chatbot 🤖
import random

responses = {
    "hello": ["Hi there!", "Hello 👋", "Hey! How’s it going?"],
    "how are you": ["I’m just code, but I’m doing great! 😎", "Feeling awesome!", "All systems running fine!"],
    "bye": ["Goodbye! 👋", "See you soon!", "Take care!"],
}

print("🤖 Chatbot: Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()
    if user == "bye":
        print("🤖 Chatbot: " + random.choice(responses["bye"]))
        break
    reply = None
    for key in responses:
        if key in user:
            reply = random.choice(responses[key])
            break
    print("🤖 Chatbot:", reply if reply else "Sorry, I didn’t understand that 🤔")
