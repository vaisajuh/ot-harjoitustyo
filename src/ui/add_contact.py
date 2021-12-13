from tkinter.messagebox import showinfo
from tkinter import ttk


class AddContact:
    def __init__(self, root, functionality, db,  session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self._add_contact = None
        self._name_entry = None
        self._address_entry = None
        self._email_entry = None
        self._phone_number_entry = None

    def destroy(self):
        self._add_contact.destroy()

    def _validate_insert_contact(self):
        validate_length = self._validate_length()
        validate_email = self._validate_email()
        validate_number = self._validate_number()
        if validate_length and validate_email and validate_number == True:
            current_session = self.session.get_session()
            self.db.contacts.insert_contact(current_session, self._name_entry.get(
            ), self._address_entry.get(), self._email_entry.get(), self._phone_number_entry.get())
            showinfo(
                title="Tiedoksi",
                message="Yhteystieto lisätty tietokantaan"
            )
        self.destroy()
        self.start_add_contact()

    def _validate_length(self):
        if len(self._name_entry.get()) not in range(3, 40) or\
                len(self._address_entry.get()) not in range(3, 40) or\
            len(self._phone_number_entry.get()) not in range(3, 40) or\
                len(self._email_entry.get()) not in range(3, 40):
            showinfo(
                title="Tiedoksi",
                message="Syötteen tulee olla neljän ja neljänkymmenen väliltä"
            )
            return False
        return True

    def _validate_email(self):
        try:
            first_letter = self._email_entry.get()[0]
            if '@' and "." not in self._email_entry.get()\
                    or first_letter == "@":
                showinfo(
                    title="Tiedoksi",
                    message="Sähköpostin tulee muodossa x@x.x"
                )
                return False
        except:
            pass
        return True

    def _validate_number(self):
        for character in self._phone_number_entry.get():
            if character.isdigit():
                return True
        showinfo(
            title="Tiedoksi",
            message="Puhelinnumerossa tulee olla vain numeroita"
        )
        return False

    def start_add_contact(self):
        self._add_contact = ttk.Frame(master=self.root)
        self._add_contact.pack(padx=10, pady=10, fill='x', expand=True)

        name_label = ttk.Label(master=self._add_contact, text="Nimi")
        name_label.pack(fill='x', expand=True)

        self._name_entry = ttk.Entry(master=self._add_contact)
        self._name_entry.pack(fill='x', expand=True)

        address_label = ttk.Label(master=self._add_contact, text="Osoite")
        address_label.pack(fill='x', expand=True)

        self._address_entry = ttk.Entry(master=self._add_contact)
        self._address_entry.pack(fill='x', expand=True)

        email_label = ttk.Label(master=self._add_contact, text="Sähköposti")
        email_label.pack(fill='x', expand=True)

        self._email_entry = ttk.Entry(master=self._add_contact)
        self._email_entry.pack(fill='x', expand=True)

        phone_number_label = ttk.Label(
            master=self._add_contact, text="Puhelinnumero")
        phone_number_label.pack(fill='x', expand=True)

        self._phone_number_entry = ttk.Entry(master=self._add_contact)
        self._phone_number_entry.pack(fill='x', expand=True)

        add_button = ttk.Button(
            master=self._add_contact, text="Lisää", command=self._validate_insert_contact)
        add_button.pack(fill='x', expand=True, pady=10)

        reverse_button = ttk.Button(
            master=self._add_contact, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.pack(fill='x', expand=True, pady=10)
