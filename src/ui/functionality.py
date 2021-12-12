from tkinter import ttk


class Functionality:
    def __init__(self, root, login, add_contact, show_contacts):
        self.root = root
        self.login = login
        self.add_contact = add_contact
        self.show_contacts = show_contacts
        self._functionality = None

    def destroy(self):
        self._functionality.destroy()

    def start_functionality(self):
        self.root.geometry('300x300')
        self._functionality = ttk.Frame(master=self.root)
        self._functionality.pack(padx=10, pady=10, fill='x', expand=True)

        get_button = ttk.Button(
            master=self._functionality, text="Hae yhteystiedot", command=self.show_contacts)
        get_button.pack(fill='x', expand=True, pady=10)

        add_button = ttk.Button(
            master=self._functionality, text="Lisää yhteystieto", command=self.add_contact)
        add_button.pack(fill='x', expand=True, pady=10)

        logout_button = ttk.Button(
            master=self._functionality, text="Kirjaudu ulos", command=self.login)
        logout_button.pack(fill='x', expand=True, pady=10)
