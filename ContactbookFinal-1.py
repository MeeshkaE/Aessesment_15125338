import tkinter as tk
from tkinter import messagebox
import json


class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    #  Returns a string representation of the contact,useful when printing contact details
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


class ContactBook:
    # Initialises an empty list of contacts
    def __init__(self):
        self.contacts = []

    #  Adds a new contact to the list of contacts and displays a success message
    def add_contact(self, contact):
        self.contacts.append(contact)
        messagebox.showinfo("Success", f"Contact {contact.name} added successfully.")
        #  Big O Notation: O(1), the time complexity is constant

    #  searches for a contact by name and returns the contact if found
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None
        # Big O Notation: O(n), the time complexity is linear

    #  Deletes a contact by name and displays a success message
    def delete_contact(self, name):
        contact_to_delete = self.search_contact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
        else:
            messagebox.showwarning("Not Found", f"Contact {name} not found.")
        # Big O Notation: O(n), the time complexity is linear

    #  searches for a contact by name and updates the contact details
    def update_contact(self, name, new_name=None, new_phone=None, new_email=None):
        contact_to_update = self.search_contact(name)
        if contact_to_update:
            if new_name:
                contact_to_update.name = new_name
            if new_phone:
                contact_to_update.phone_number = new_phone
            if new_email:
                contact_to_update.email = new_email
            messagebox.showinfo("Success", f"Contact {name} updated sucessfully")
        else:
            messagebox.showwarning("Not Found", f"Contact {name} not found.")
            # Big O Notation: O(n), the time complexity is linear

    #  Displays all contacts in the contact book
    def display_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
        else:
            contacts_str = "\n".join(str(contact) for contact in self.contacts)
            messagebox.showinfo("Contacts", contacts_str)
            #  Big O Notation: O(n), the time complexity is linear

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json_contacts = [contact.__dict__ for contact in self.contacts]
            json.dump(json_contacts, f, indent=4)
            messagebox.showinfo("Success", "Contacts saved successfully.")
            #  Big O Notation: O(n), the time complexity is linear
            
    def end (self):
        root.quit()
        root.destroy()
        #  ends the program
        #  Big O(1) as it only quits the program

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                json_contacts = json.load(f)
                self.contacts = [Contact(**data) for data in json_contacts]
        except FileNotFoundError:
            self.contact_book = []
            messagebox.showwarning("Not Found", "No contacts found.")
            #  Big O Notation: O(n), the time complexity is linear
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding contacts.")
            #  Big O Notation: O(n), the time complexity is linear


#  Creates a GUI application for the contact book using tkinter
class ContactBookApp:
    #  initialises the contact book application with a
    def __init__(self, root):
        self.contact_book = ContactBook()
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(bg="violet")

        # Add Contact Section
        self.create_add_contact_section()

        # Search Contact Section
        self.create_search_contact_section()

        # Display Contacts Section
        self.create_display_contacts_section()

        # Delete Contact Section
        self.create_delete_contact_section()

        # Update Contact Section
        self.create_update_contact_section()

        self.create_save_contacts_section()

        # Result Display
        self.result_text = tk.Text(
            root, height=10, width=60, bg="light grey", font=("Arial", 12)
        )
        self.result_text.grid(row=19, column=0, columnspan=3, pady=10, padx=10)

        self.create_quit_button()
        #  Big O Notation: O(1), the time complexity is constant

    #  each of these sections creates a section of the GUI for a specific task
    def create_add_contact_section(self):
        #  creates labels, entry fields and buttons for adding a contact
        tk.Label(
            self.root, text="Adding a contact ", bg="white", font=("Arial", 14, "bold"), width=20
        ).grid(row=0, column=0, columnspan=3, pady=10)
        tk.Label(self.root, text="Name", bg="white", width=20).grid(row=1, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=1, column=1, padx=5)

        tk.Label(self.root, text="Phone Number", bg="white", width=20).grid(row=2, column=0)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=2, column=1, padx=10)

        tk.Label(self.root, text="Email", bg="white", width=20).grid(row=3, column=0)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=3, column=1, padx=5)

        tk.Button(
            self.root,
            text="Add Contact",
            command=self.add_contact,
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=4, column=0, columnspan=3, pady=10)

    def create_search_contact_section(self):
        tk.Label(
            self.root,
            text="Searching for a Contact",
            bg="white",
            font=("Arial", 14, "bold"),
        ).grid(row=5, column=0, columnspan=3, pady=10)
        tk.Label(self.root, text="  Name    ", bg="white", width=20).grid(row=6, column=0)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=6, column=1, padx=5)
        tk.Button(
            self.root,
            text="Search Contact",
            command=self.search_contact,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=7, column=0, columnspan=3, pady=10)

    def create_display_contacts_section(self):
        tk.Button(
            self.root,
            text="Display All Contacts",
            command=self.display_contacts,
            bg="orange",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=8, column=0, columnspan=3, pady=10)

    def create_delete_contact_section(self):
        tk.Label(
            self.root, text="Deleting a Contact", bg="white", font=("Arial", 14, "bold")
        ).grid(row=9, column=0, columnspan=3, pady=10)
        tk.Label(self.root, text="Name", bg="white", width=20).grid(row=10, column=0)
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.grid(row=10, column=1, padx=5)
        tk.Button(
            self.root,
            text="Delete Contact",
            command=self.delete_contact,
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=11, column=0, columnspan=3, pady=10)

    def create_quit_button(self):
        self.quit_button = tk.Button(
            self.root,
            text="Exit",
            command=self.root.quit,
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.quit_button.grid(row=20, column=0, columnspan=3, pady=10)
    #  creates the update contact section of the GUI

    def create_update_contact_section(self):

        tk.Label(
            self.root, text="Updating a Contact", bg="white", font=("Arial", 14, "bold"), width=20
        ).grid(row=12, column=0, columnspan=3, pady=10)
        tk.Label(self.root, text="Name", bg="white", width=20).grid(row=13, column=0)
        self.update_name_entry = tk.Entry(self.root)
        self.update_name_entry.grid(row=13, column=1, padx=5)

        tk.Label(self.root, text="New Name", bg="white", width=20).grid(row=14, column=0)
        self.update_new_name_entry = tk.Entry(self.root)
        self.update_new_name_entry.grid(row=14, column=1, padx=5)

        tk.Label(self.root, text="New Phone Number", bg="white", width=20).grid(row=15, column=0)
        self.update_phone_entry = tk.Entry(self.root)
        self.update_phone_entry.grid(row=15, column=1, padx=5)

        tk.Label(self.root, text="New Email", bg="white", width=20).grid(row=16, column=0)
        self.update_email_entry = tk.Entry(self.root)
        self.update_email_entry.grid(row=16, column=1, padx=5)

        tk.Button(
            self.root,
            text="Update Contact",
            command=self.update_contact,
            bg="grey",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=17, column=0, columnspan=3, pady=10)

    def create_save_contacts_section(self):
        tk.Button(
            self.root,
            text="Save Contacts",
            command=self.save_contacts,
            bg="purple",
            fg="white",
            font=("Arial", 12, "bold"),
        ).grid(row=18, column=0, columnspan=3, pady=10)

    def create_quit_button(self):
        self.quit_button = tk.Button(
            self.root,
            text="Exit",
            command=self.contact_book.end,
            bg="red",
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.quit_button.grid(row=18, column=1, columnspan=3, pady=10)
    #  Gets the contact details from the entry fields and adds the contact to the contact book & displays the result in the result text box
    
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contact_book.add_contact(contact)
            self.result_text.insert(tk.END, f"Added: {contact}\n")
            self.clear_entries(self.entry_name, self.entry_phone, self.entry_email)
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    #  This deals with searching for a contact by name and displaying the result in the result text box
    def search_contact(self):
        name = self.search_entry.get()
        contact = self.contact_book.search_contact(name)
        self.result_text.delete(1.0, tk.END)
        if contact:
            self.result_text.insert(tk.END, f"Found: {contact}\n")
        else:
            self.result_text.insert(tk.END, "Contact not found\n")
        self.clear_entries(self.search_entry)

    def save_contacts(self):
        self.contact_book.save_contacts()
        self.result_text.insert(tk.END, "Contacts saved successfully\n")

    def delete_contact(self):
        name = self.delete_entry.get()
        self.contact_book.delete_contact(name)
        self.result_text.insert(tk.END, f"Deleted: {name}\n")
        self.clear_entries(self.delete_entry)

    def update_contact(self):
        name = self.update_name_entry.get()
        new_name = self.update_new_name_entry.get()
        new_phone = self.update_phone_entry.get()
        new_email = self.update_email_entry.get()
        self.contact_book.update_contact(name, new_name, new_phone, new_email)
        self.result_text.insert(tk.END, f"Updated: {name}\n")
        self.clear_entries(
            self.update_name_entry,
            self.update_new_name_entry,
            self.update_phone_entry,
            self.update_email_entry,
        )

    def display_contacts(self):
        self.result_text.delete(1.0, tk.END)
        contacts_str = "\n".join(str(contact) for contact in self.contact_book.contacts)
        self.result_text.insert(
            tk.END, contacts_str if contacts_str else "No contacts found\n"
        )
#  this method clears the entry fields after an operation is performed

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)


#  This is the main method that runs the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    app.contact_book.load_contacts()
    root.mainloop()
