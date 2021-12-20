from tkinter import Entry, ttk
from tkinter.constants import CENTER, END
from tkinter import Tk



class ShowContacts:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self.update_view = None
        self._show_contacts = None
        self._edit_buttons = None
        self._tree = None
        self._search_contacts = None
        self._name_entry = None
        self._address_entry = None
        self._email_entry = None
        self._phone_number_entry = None

    def destroy(self):
        self._show_contacts.destroy()
        self._search_contacts.destroy()
        self._edit_buttons.destroy()
        if self.update_view is not None:
            self.update_view.destroy()

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
            self.update_view.destroy()
            self.update_view = None
            self.destroy()
            self.start_show_contacts()
        except:
            pass
    
    def _edit_button(self):
        try:
            row_value = self._tree.focus()
            row_id = int(self._tree.item(row_value)["text"])
            get_row = self.db.contacts.get_row(row_id)
            self._update_view(get_row, row_id)
        except:
            pass

    def _update_view(self, row, row_id):
        if self.update_view is None:
            self.update_view = Tk()
            self.update_view.geometry('300x300')
            self.update_view.title('Muokkaa')
        
            user_entries = ttk.Frame(master=self.update_view)
            user_entries.pack(padx=10, pady=10, fill='x', expand=True)

            name_label = ttk.Label(master=user_entries, text="Nimi")
            name_label.pack(fill='x', expand=True)

            name = Entry(user_entries)
            name.insert(END, row[0])
            name.pack(fill='x', expand=True)

            address_label = ttk.Label(master=user_entries, text="Osoite")
            address_label.pack(fill='x', expand=True)

            address = Entry(user_entries)
            address.insert(END, row[1])
            address.pack(fill='x', expand=True)

            email_label = ttk.Label(master=user_entries, text="Email")
            email_label.pack(fill='x', expand=True)

            email = Entry(user_entries)
            email.insert(END, row[2])
            email.pack(fill='x', expand=True)

            phone_number_label = ttk.Label(master=user_entries, text="Puhelinnumero")
            phone_number_label.pack(fill='x', expand=True)

            number = Entry(user_entries)
            number.insert(END, row[3])
            number.pack(fill='x', expand=True)

            add_button = ttk.Button(
                master=user_entries, text="Muokkaa", command=lambda: self._update_contact(row_id, name.get(), address.get(), email.get(), number.get()))
            add_button.pack(fill='x', expand=True, pady=10)

            self.update_view.mainloop()

    def _update_contact(self, row_id, name, address, email, number):
        self.db.contacts.update_row(row_id, name, address, email, number)
        self.destroy()
        self.update_view = None
        self.start_show_contacts()

    def start_show_contacts(self):
        self.root.geometry('')
        self._show_contacts = ttk.Frame(master=self.root)
        self._show_contacts.grid()
        self._search_fuctionality()
        self._edit_contacts()
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
    
    def _edit_contacts(self):
        self._edit_buttons = ttk.Frame(master=self.root)
        self._edit_buttons.grid(row=1, column=0)
        
        delete_button = ttk.Button(
            master=self._edit_buttons, text="Poista", command=self._delete_button)
        delete_button.grid(row=0, column=0, padx=10, pady=10)

        edit_button = ttk.Button(
            master=self._edit_buttons, text="Muokkaa", command=self._edit_button)
        edit_button.grid(row=0, column=1, padx=10, pady=10)

        reverse_button = ttk.Button(
            master=self._edit_buttons, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.grid(row=0, column=3, padx=10, pady=10)


    
    def _search_fuctionality(self):
        self._search_contacts = ttk.Frame(master=self.root)
        self._search_contacts.grid(row=0, column=2)
        
        name_label = ttk.Label(master=self._search_contacts, text="Nimi")
        name_label.grid(row=1, padx=5, pady=3)
        
        self._name_entry = ttk.Entry(master=self._search_contacts)
        self._name_entry.grid(row=2, padx=5, pady=3)
        
        address_label = ttk.Label(master=self._search_contacts, text="Osoite")
        address_label.grid(row=3, padx=5, pady=3)
        
        self._address_entry = ttk.Entry(master=self._search_contacts)
        self._address_entry.grid(row=4, padx=5, pady=3)

        email_label = ttk.Label(master=self._search_contacts, text="Sähköposti")
        email_label.grid(row=5, padx=5, pady=3)
        
        self._email_entry = ttk.Entry(master=self._search_contacts)
        self._email_entry.grid(row=6, padx=5, pady=3)

        phone_number_label = ttk.Label(master=self._search_contacts, text="Puhelinnumero")
        phone_number_label.grid(row=7, padx=5, pady=3)
        
        self._phone_number_entry = ttk.Entry(master=self._search_contacts)
        self._phone_number_entry.grid(row=8, padx=5, pady=3)

        search_button = ttk.Button(master=self._search_contacts, text="Hae", command=self._insert_contacts)
        search_button.grid(row=9, padx=5, pady=3)
