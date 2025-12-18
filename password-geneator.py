import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("--- Professional Password Generator ---")
try:
    len_input = int(input("What is the number of your password? (like: 12): "))
    if len_input < 8:
        print("Please use 8 character for your security.")
    else:
        new_pass = generate_password(len_input)
        print(f"Your new Passworsd: {new_pass}")
except ValueError:
    print("Please enter your password:")