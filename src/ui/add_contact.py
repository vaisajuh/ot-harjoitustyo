from tkinter.messagebox import showinfo
from tkinter import ttk


class AddContact:
    def __init__(self, root, functionality, db,  session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self.add_contact = None
        self.name_entry = None
        self.address_entry = None
        self.email_entry = None
        self.phone_number_entry = None

    def destroy(self):
        self.add_contact.destroy()

    def validate_insert_contact(self):
        validate_length = self.validate_length()
        validate_email = self.validate_email()
        validate_number = self.validate_number()
        if validate_length and validate_email and validate_number == True:
            current_session = self.session.get_session()
            self.db.contacts.insert_contact(current_session, self.name_entry.get(
            ), self.address_entry.get(), self.email_entry.get(), self.phone_number_entry.get())
            showinfo(
                title="Tiedoksi",
                message="Yhteystieto lisätty tietokantaan"
            )
        self.destroy()
        self.start_add_contact()
    
    def validate_length(self):
        if len(self.name_entry.get()) not in range(4, 40) or\
            len(self.address_entry.get()) not in range(4,40) or\
                len(self.phone_number_entry.get()) not in range(4,40) or\
                    len(self.email_entry.get()) not in range(4,40):
                    showinfo(
                        title="Tiedoksi",
                        message="Syötteen tulee olla neljän ja neljänkymmenen väliltä"
                        )
                    return False
        return True
    
    def validate_email(self):
        try:
            first_letter = self.email_entry.get()[0]
            if '@' and "." not in self.email_entry.get()\
                or first_letter == "@":
                showinfo(
                    title="Tiedoksi",
                    message="Sähköpostin tulee muodossa x@x.x"
                )
                return False
        except:
            pass
        return True
    
    def validate_number(self):
        for character in self.phone_number_entry.get():
            if character.isdigit():
                return True
        showinfo(
            title="Tiedoksi",
            message="Puhelinnumerossa tulee olla vain numeroita"
        )
        return False

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

        phone_number_label = ttk.Label(
            master=self.add_contact, text="Puhelinnumero")
        phone_number_label.pack(fill='x', expand=True)

        self.phone_number_entry = ttk.Entry(master=self.add_contact)
        self.phone_number_entry.pack(fill='x', expand=True)

        add_button = ttk.Button(
            master=self.add_contact, text="Lisää", command=self.validate_insert_contact)
        add_button.pack(fill='x', expand=True, pady=10)

        reverse_button = ttk.Button(
            master=self.add_contact, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.pack(fill='x', expand=True, pady=10)
