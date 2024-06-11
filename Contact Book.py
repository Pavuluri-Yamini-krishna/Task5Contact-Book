class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))
        print("Successfully added contact to the list!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts have been included.")
            return
        print("\nContact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name}, {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts have been included.")
            return
        print("\nSearch Results:")
        for contact in found_contacts:
            print(contact)

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            self.contacts[index].update(name, phone, email, address)
            print("Updated of contact was successful!")
        else:
            print("Index of Contact is not valid .")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Successfully deleted the contact from the list!")
        else:
            print("Index of Contact is not valid .")

    def run(self):
        while True:
            print("\n===== Contact Manager =====")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your Selection: ").strip()

            if choice == '1':
                name = input("Enter Contact Name: ").strip()
                phone = input("Enter Mobile number: ").strip()
                email = input("Enter Email: ").strip()
                address = input("Enter Address: ").strip()
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                search_term = input("Enter Contact name or Contact number to search: ").strip()
                self.search_contact(search_term)
            elif choice == '4':
                try:
                    index = int(input("Enter the index of contact to update: ")) - 1
                    name = input("Enter New Name (If current,leave blank):").strip() or None
                    phone = input("Enter New Mobile number (If current,leave blank): ").strip() or None
                    email = input("Enter New Email (If current,leave blank): ").strip() or None
                    address = input("Enter New Address (If current,leave blank): ").strip() or None
                    self.update_contact(index, name, phone, email, address)
                except ValueError:
                    print("Please re-enter the input with a valid number.")
            elif choice == '5':
                try:
                    index = int(input("Input the contact index to be deleted: ")) - 1
                    self.delete_contact(index)
                except ValueError:
                    print("Kindly input a valid number. Please input a valid number.")
            elif choice == '6':
                print("Logging out of Contact Manager.")
                break
            else:
                print("Please select valid option and try once more")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
