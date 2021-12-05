from tkinter import ttk
from tkinter.constants import CENTER


class ShowContacts:
    def __init__(self, root, functionality, db, session):
        self.root = root
        self.functionality = functionality
        self.db = db
        self.session = session
        self.show_contacts = None
        self.tree = None


    def destroy(self):
        self.show_contacts.destroy()


    def insert_contacts(self):
        get_contacts = self.db.contacts.get_contacts(
            self.session.get_session())
        for i in get_contacts:
            ind = i[4]
            self.tree.insert('', 'end', text=ind,
                             values=(i[0], i[1], i[2], i[3]))
            
            
    def remove_button(self):
        try:
            row_value = self.tree.focus()
            row_id = int(self.tree.item(row_value)["text"])
            self.db.contacts.delete_contact(row_id)
            self.destroy()
            self.start_show_contacts()
        except:
            pass

    def start_show_contacts(self):
        self.root.geometry('')
        self.show_contacts = ttk.Frame(master=self.root)
        self.show_contacts.grid()
        self.tree = ttk.Treeview(master=self.show_contacts, column=(
            "Nimi", "Osoite", "Email", "Puhelinnumero"), show='headings')
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="Nimi")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Osoite")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Email")
        self.tree.column("# 4", anchor=CENTER)
        self.tree.heading("# 4", text="Puhelinnumero")
        self.insert_contacts()
        self.tree.grid(row=0)
        remove_button = ttk.Button(
            master=self.show_contacts, text="Poista", command=self.remove_button)
        remove_button.grid()
        reverse_button = ttk.Button(
            master=self.show_contacts, text="Palaa edelliseen näkymään", command=self.functionality)
        reverse_button.grid()
