import os

print("1. Shutdown Computer Immediately")
print("2. Restart Computer Immediately")
print("3. Exit")

choice = input("Please choose your favorite (1/2/3): ")

if choice == '1':
    os.system("shutdown /s /t 1")
elif choice == '2':
    os.system("shutdown /r /t 1")
elif choice == '3':
    exit()
else:
    print("Wrong Input!")