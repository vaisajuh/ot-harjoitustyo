from tkinter import Toplevel, ttk
from tkinter.constants import CENTER, N
from typing import Text


class ShowContacts:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self._show_contacts = None
        self._tree = None
        self._search_contacts = None
        self._name_entry = None
        self._address_entry = None
        self._email_entry = None
        self._phone_number_entry = None

    def destroy(self):
        self._show_contacts.destroy()
        self._search_contacts.destroy()

    def _insert_contacts(self):
        for i in self._tree.get_children():
            self._tree.delete(i)
        get_contacts = self.db.contacts.get_contacts(
            self.session.get_session(), self._email_entry.get(), self._address_entry.get(),
            self._email_entry.get(), self._phone_number_entry.get())
        for i in get_contacts:
            ind = i[4]
            self._tree.insert('', 'end', text=ind,
                             values=(i[0], i[1], i[2], i[3]))

    def _delete_button(self):
        try:
            row_value = self._tree.focus()
            row_id = int(self._tree.item(row_value)["text"])
            self.db.contacts.delete_contact(row_id)
            self.destroy()
            self.start_show_contacts()
        except:
            pass

    def start_show_contacts(self):
        self.root.geometry('')
        self._show_contacts = ttk.Frame(master=self.root)
        self._show_contacts.grid()
        self.search_contacts()
        self._tree = ttk.Treeview(master=self._show_contacts, column=(
            "Nimi", "Osoite", "Email", "Puhelinnumero"), show='headings')
        self._tree.column("# 1", anchor=CENTER)
        self._tree.heading("# 1", text="Nimi")
        self._tree.column("# 2", anchor=CENTER)
        self._tree.heading("# 2", text="Osoite")
        self._tree.column("# 3", anchor=CENTER)
        self._tree.heading("# 3", text="Email")
        self._tree.column("# 4", anchor=CENTER)
        self._tree.heading("# 4", text="Puhelinnumero")
        self._insert_contacts()
        self._tree.grid()

    
    def search_contacts(self):
        self._search_contacts = ttk.Frame(master=self.root)
        self._search_contacts.grid(row=0, column=1)

        delete_button = ttk.Button(
            master=self._search_contacts, text="Poista", command=self._delete_button)
        delete_button.grid(row=1, column=1)

        reverse_button = ttk.Button(
            master=self._search_contacts, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.grid(row=10, column=1)
        
        name_label = ttk.Label(master=self._search_contacts, text="Nimi")
        name_label.grid(row=1)
        
        self._name_entry = ttk.Entry(master=self._search_contacts)
        self._name_entry.grid(row=2)
        
        address_label = ttk.Label(master=self._search_contacts, text="Osoite")
        address_label.grid(row=3)
        
        self._address_entry = ttk.Entry(master=self._search_contacts)
        self._address_entry.grid(row=4)

        email_label = ttk.Label(master=self._search_contacts, text="Sähköposti")
        email_label.grid(row=5)
        
        self._email_entry = ttk.Entry(master=self._search_contacts)
        self._email_entry.grid(row=6)

        phone_number_label = ttk.Label(master=self._search_contacts, text="Puhelinnumero")
        phone_number_label.grid(row=7)
        
        self._phone_number_entry = ttk.Entry(master=self._search_contacts)
        self._phone_number_entry.grid(row=8)

        search_button = ttk.Button(master=self._search_contacts, text="Hae", command=self._insert_contacts)
        search_button.grid(row=9)
