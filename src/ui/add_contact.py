from tkinter import ttk

class AddContact:
    def __init__(self, root, functionality):
        self.root = root
        self.functionality = functionality
        self.add_contact = None
        self.name_entry = None
        self.address_entry = None
        self.email_entry = None
        self.phone_number_entry = None
    
    
    def destroy(self):
        self.add_contact.destroy()
    

    def start_add_contact(self):
        self.add_contact = ttk.Frame(master=self.root)
        self.add_contact.pack(padx=10, pady=10, fill='x', expand=True)

        name_label = ttk.Label(master=self.add_contact, text="Nimi")
        name_label.pack(fill='x', expand=True)

        self.name_entry = ttk.Entry(master=self.add_contact)
        self.name_entry.pack(fill='x', expand=True)

        address_label = ttk.Label(master=self.add_contact, text="Osoite")
        address_label.pack(fill='x', expand=True)

        self.address_entry = ttk.Entry(master=self.add_contact)
        self.address_entry.pack(fill='x', expand=True)

        email_label = ttk.Label(master=self.add_contact, text="Sähköposti")
        email_label.pack(fill='x', expand=True)

        self.email_entry = ttk.Entry(master=self.add_contact)
        self.email_entry.pack(fill='x', expand=True)

        phone_number_label = ttk.Label(master=self.add_contact, text="Puhelinnumero")
        phone_number_label.pack(fill='x', expand=True)

        self.phone_number_entry = ttk.Entry(master=self.add_contact)
        self.phone_number_entry.pack(fill='x', expand=True)

        add_button = ttk.Button(master=self.add_contact, text="Lisää", command="")
        add_button.pack(fill='x', expand=True, pady=10)

        reverse_button = ttk.Button(master=self.add_contact, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.pack(fill='x', expand=True, pady=10)
        




