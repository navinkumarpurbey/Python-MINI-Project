import requests
import random

url = "https://official-joke-api.appspot.com/jokes/programming/ten"
response = requests.get(url)
jokes = response.json()

print("Random Programming Joke 🤣")
jokes = random.choice(jokes)
print(jokes['setup'])
print("", jokes['punchline'])