import random
import string

def generate_random_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password of length 12
random_password = generate_random_password(12)
print("Random Password:", random_password)
