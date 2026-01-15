import random

computer_number = random.randint(1, 50)
attempts = 0

print("--- Number Guessing Game ---")
print("Ami 1 theke 50 er moddhe ekti songkhya bhebechi. Bolun to seta koto?")

while True:
    guess = int(input("\nApnar guess likhun: "))
    attempts += 1
    
    if guess < computer_number:
        print("Aro boro songkhya guess korun!")
    elif guess > computer_number:
        print("Aro choto songkhya guess korun!")
    else:
        print(f"Abhinandan! Tumi {attempts} bar chesta kore sothik uttor diyecho.")
        break 