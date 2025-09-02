# Generate the Random Password Genarator
# using Python 😻😻😻

import random
import string

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Now go through the examples
print(" Your Random Password is: ", generate_password(12))

