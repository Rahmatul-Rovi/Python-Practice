import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

size = int(input("Koto boro password chai? (e.g., 12): "))

if size < 4:
    print("Security-r jonno password ontoto 4 digit-er hote hobe!")
else:
    new_password = password_generator(size)
    print(f"Apnar secure password holo: {new_password}")