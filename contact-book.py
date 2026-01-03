# contact_book.py

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"\n✅ Contact for {name} saved successfully!")

def view_contacts():
    if not contacts:
        print("\n📭 Contact list is empty.")
        return
    
    print("\n--- 👥 ALL CONTACTS ---")
    for index, person in enumerate(contacts, start=1):
        print(f"{index}. Name: {person['name']} | Phone: {person['phone']} | Email: {person['email']}")

def search_contact():
    search_name = input("\nEnter the name to search: ").lower()
    found = False
    
    for person in contacts:
        if person['name'].lower() == search_name:
            print(f"\n🔍 Found: {person['name']} - {person['phone']} ({person['email']})")
            found = True
            break
            
    if not found:
        print("\n❌ No contact found with that name.")

def delete_contact():
    name_to_del = input("\nEnter name to delete: ").lower()
    global contacts
    # Filtering logic (JS/TS er filter er moto)
    new_list = [p for p in contacts if p['name'].lower() != name_to_del]
    
    if len(new_list) < len(contacts):
        contacts = new_list
        print("\n🗑️ Contact deleted!")
    else:
        print("\n❌ Contact not found.")

# --- Main Menu ---
while True:
    print("\n--- 📱 CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Select an option: ")
    
    if choice == '1': add_contact()
    elif choice == '2': view_contacts()
    elif choice == '3': search_contact()
    elif choice == '4': delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")