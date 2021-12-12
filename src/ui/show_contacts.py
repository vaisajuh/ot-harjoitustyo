from tkinter import ttk
from tkinter.constants import CENTER


class ShowContacts:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self._show_contacts = None
        self._tree = None

    def destroy(self):
        self._show_contacts.destroy()

    def _insert_contacts(self):
        get_contacts = self.db.contacts.get_contacts(
            self.session.get_session())
        for i in get_contacts:
            ind = i[4]
            self._tree.insert('', 'end', text=ind,
                             values=(i[0], i[1], i[2], i[3]))

    def _remove_button(self):
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
        remove_button = ttk.Button(
            master=self._show_contacts, text="Poista", command=self._remove_button)
        remove_button.grid(column=1)
        reverse_button = ttk.Button(
            master=self._show_contacts, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.grid()
