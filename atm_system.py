# atm_system.py

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\n💰 Current Balance: {self.balance} BDT")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Successfully deposited {amount} BDT")
        else:
            print("❌ Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ Successfully withdrawn {amount} BDT")
        elif amount > self.balance:
            print("❌ Insufficient balance!")
        else:
            print("❌ Invalid amount!")

my_atm = ATM(1000)  

while True:
    print("\n--- 🏧 WELCOME TO PYTHON BANK ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == '1':
        my_atm.check_balance()
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        my_atm.deposit(amt)
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        my_atm.withdraw(amt)
    elif choice == '4':
        print("👋 Thank you for using our ATM. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")